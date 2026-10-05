from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Optional, Literal
import httpx
import ssl
import truststore
from langgraph.graph import START, END, StateGraph
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
load_dotenv(override = True)




class GraphState(BaseModel):
    user_input : str = Field(description="The user input to the graph.")
    decision: Optional[Literal["story", "joke"]] = Field(default=None, description="The decision of the graph.")
    final_output: Optional[str] = Field(default=None, description="The final output of the graph.")

http_client = httpx.Client(
    verify=truststore.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
)
llm = ChatGroq(
    model="qwen/qwen3.8-27b",
    temperature=0.8,
    http_client=http_client,
)

def validator(state: GraphState):
    user_input = state.user_input
    prompt = PromptTemplate(
        template="""
        You are a helpful AI assistant. Determine whether the user wants a story or a joke.
        Reply with only one word: story or joke.
        User input: {user_input}
        """,
        input_variables=["user_input"],
    )
    chain = prompt | llm
    response = chain.invoke({"user_input": user_input})
    return {"decision": response.content}
    

def router(state : GraphState):
    decision = state.decision
    
    if decision == "story":
        return "story"
    else:
        return "joke"
    
def story_node(state: GraphState):
    prompt = PromptTemplate(
        template="Tell me a random story based on this user input. No longer than 100 words.\nUser input: {user_input}",
        input_variables=["user_input"],
    )
    chain = prompt | llm
    response = chain.invoke({"user_input": state.user_input})
    return {"final_output": response.content}
    
    
def joke_node(state: GraphState):
    prompt = PromptTemplate(
        template="Tell me a random joke based on this user input. No longer than 100 words.\nUser input: {user_input}",
        input_variables=["user_input"],
    )
    chain = prompt | llm # 把提示模板和語言模型串接起來，建立一條處理流程。這裡的 | 是 LangChain 的管線運算子，不是一般的位元運算。
    # 例如收到 模型輸入 {"user_input": "Tell me a joke"}
    # prompt 會生成對應的模型輸入，然後通過 chain 發送給語言模型，最終得到 response。
    
    response = chain.invoke({"user_input": state.user_input})
    return {"final_output": response.content} 
        

builder = StateGraph(GraphState)
builder.add_node("validator", validator)


builder.add_node("story_node", story_node)
builder.add_node("joke_node", joke_node)
builder.add_edge(START, "validator") #告訴 LangGraph：執行這張圖時，第一個要跑的節點是 validator
builder.add_conditional_edges("validator", router,{
    "story": "story_node",
    "joke": "joke_node"
}) 

builder.add_edge("story_node", END)
builder.add_edge("joke_node", END)

graph = builder.compile()

response = graph.invoke({"user_input": "Tell me a joke"}) # 傳入初始訊息並執行整張 Graph，是同步的

print(response)