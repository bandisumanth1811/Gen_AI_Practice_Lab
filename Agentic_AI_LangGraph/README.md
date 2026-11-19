# Agentic AI with LangGraph

Hands-on notebooks and scripts for building agents with LangGraph, from a basic chatbot to tool-using and multi-agent systems.

## Contents

| Folder | What it covers |
|--------|----------------|
| `1. Basic Chatbot` | `StateGraph` chatbot, adding tools, ReAct agent architecture, memory with checkpointers, sync/async streaming |
| `2. Debugging and Monitoring` | LangSmith tracing (`Tracing.ipynb`) and a tool-calling agent served in LangGraph Studio (`lg_studio_tracing.py`, `langgraph.json`) |
| `3. mcpdemolangchain` | MCP demo: a math server (stdio), a weather server (streamable HTTP) and a LangChain client that gives both to a ReAct agent |
| `4. Multiagent` | Multi-agent workflows and a supervisor agent that routes work between agents |
| `api_test.py` | Small FastAPI app for practicing API endpoints |

## Tech
Python 3.10+, LangGraph, LangChain, LangSmith, MCP (`langchain-mcp-adapters`), Groq, Tavily, FastAPI

## Setup
The project uses [uv](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/bandisumanth1811/Gen_AI_Practice_Lab.git
cd Gen_AI_Practice_Lab/Agentic_AI_LangGraph
uv sync
```

Without uv: `python -m venv .venv`, activate it, then `pip install -r requirements.txt`.

Copy `.env.example` to `.env` and fill in your own keys (`.env` is git-ignored):

```
OPENAI_API_KEY=
LANGCHAIN_API_KEY=
Google_API_KEY=
GROQ_API_KEY=
Tavily_API_KEY=
```

## Running

LangGraph Studio:
```bash
cd "2. Debugging and Monitoring"
langgraph dev
```

MCP demo (start the weather server in one terminal, then the client in another):
```bash
cd "3. mcpdemolangchain"
python weather.py
python client.py
```

The notebooks run in Jupyter or VS Code with the project's `.venv` as the kernel.

## Notes
- Keys are loaded from `.env`; none are committed.
- Local state (`.langgraph_api/`, virtual environments) is excluded through `.gitignore`.
