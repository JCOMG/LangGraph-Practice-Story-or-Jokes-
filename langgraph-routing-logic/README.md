# 🧠 langgraph-routing-logic

_Design Smarter AI Workflows with Intent-Based Routing in LangGraph_

[![last commit](https://img.shields.io/github/last-commit/yourusername/langgraph-routing-logic?style=flat-square)](https://github.com/yourusername/langgraph-routing-logic)
[![License](https://img.shields.io/github/license/yourusername/langgraph-routing-logic?style=flat-square)](https://github.com/quikcss/langgraph-routing-logic/blob/main/LICENSE)
[![Python](https://img.shields.io/badge/python-100%25-blue?style=flat-square)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/langchain-✓-orange?style=flat-square)](https://www.langchain.com/)
[![LangGraph](https://img.shields.io/badge/langgraph-✓-purple?style=flat-square)](https://github.com/langchain-ai/langgraph)
[![uv](https://img.shields.io/badge/uv-pkg-blueviolet?style=flat-square)](https://github.com/astral-sh/uv)

---

## 🚀 Overview

**`langgraph-routing-logic`** demonstrates how to build an intent-aware AI workflow using the **Routing Logic** pattern in LangGraph.  
Think of it like a traffic cop: based on what the user says, the app sends the request down the correct lane – tell a story, crack a joke, or translate a sentence.

### ✨ Why Routing Logic?

- 🛣️ Cleanly separate functionality based on user intent  
- 🔀 Route requests dynamically in real-time  
- 📈 Scale your agent with more tools (like summarize, search, etc.)  
- 🧠 Works great with both basic logic and LLM-based validation

---

## 📂 Project Structure

```bash
.
├── main.py              # Entry point with routing logic graph
├── .env                 # Environment variables (e.g., GROQ_API_KEY)
├── pyproject.toml       # Project metadata and dependencies
├── uv.lock              # Lock file (if using uv)
└── README.md            # This file
```

---

## ⚙️ Getting Started

1. Clone the repository

```bash
git clone https://github.com/yourusername/langgraph-routing-logic.git
cd langgraph-routing-logic
```

2. Create a virtual environment and activate it

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

3.Install dependencies (with uv or pip)

```bash
uv pip install -r requirements.txt
# OR
uv venv && uv pip install -e .
```

4.Add your Groq API key to a .env file

```bash
GROQ_API_KEY=your_groq_api_key_here
```

---

## 🧠 How It Works

This project uses LangGraph to route input requests based on what the user says. It uses a simple validator that decides whether the user wants:
```
1.📖 A story
2.😂 A joke
```
Each type of request gets routed to its own node, and all flows lead to the END node – creating a clean, testable AI pipeline.

---

## 📦 Dependencies

```bash
langgraph
langchain
langchain-groq
grandalf
python-dotenv
langgraph-cli
```

---

## 📺 Video Tutorial

Watch the full walkthrough on YouTube:
🔗 https://youtu.be/cPkLKrLYSNg

---

## 📜 License

This project is licensed under the MIT License.
Feel free to use, modify, and share it.
