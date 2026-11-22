# GenAI Practice Lab

Hands-on practice with Generative AI, built topic by topic: LLM apps, RAG, and model serving. This repo is a learning log with code, notes, and my own extensions.

## What's inside

| Folder | Topic | Highlights |
|--------|-------|------------|
| `03-langchain/GROQ` | LCEL chains and model serving | Prompt, model, and parser chains with LangChain Expression Language on Groq, plus a `serve.py` API |
| `03-langchain/Langchain RAG` | Retrieval-Augmented Generation | Data ingestion, embeddings, and vector stores with FAISS and Chroma |
| `03-langchain/Ollama` | Local models | A small app running a model locally through Ollama |
| `Agentic_AI_LangGraph` | Agents with LangGraph | Chatbots, tools, memory, streaming, LangSmith tracing, LangGraph Studio, MCP clients and multi-agent supervisors |
| `Langchain Updated Version V1` | LangChain v1 | Notebooks on LangChain intro, model integration, tools and messages |
| `Langchain_Projects` | LangChain mini projects | `1. Q&A Chatbot`: a Streamlit chatbot on Groq with model, temperature and token controls and LangSmith tracking |
| `Langchain_Projects/2. Ollama Chatbot` | Local LLM chatbot | A Streamlit chatbot running `gemma:2b` locally through Ollama, no API key needed |

## Tech
Python, LangChain, LangGraph, LangSmith, MCP, Groq, Tavily, Ollama, FAISS, ChromaDB, OpenAI and Gemini APIs, Jupyter

## Progress
- [x] LangChain basics and LCEL chains
- [x] Data ingestion and embeddings
- [x] Vector stores: FAISS and Chroma
- [x] Serving a chain as an API
- [x] Running models locally with Ollama
- [x] LLM basics and prompt engineering
- [x] Agents and tools (LangGraph)
- [x] Evaluation and guardrails
- [x] Deployment with FastAPI

## Run locally
```bash
git clone https://github.com/bandisumanth1811/Gen_AI_Practice_Lab.git
cd Gen_AI_Practice_Lab/03-langchain
python -m venv venv
venv\Scripts\activate          # macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
```
Create a `.env` file in `03-langchain` with your own keys (this file is never committed):
```
GROQ_API_KEY=
OPENAI_API_KEY=
GOOGLE_API_KEY=
```

For the LangGraph project, see [`Agentic_AI_LangGraph/README.md`](Agentic_AI_LangGraph/README.md).

## Notes
- API keys are read from environment variables. None are stored in this repo.
- Generated files (vector indexes, caches) are excluded through `.gitignore`.

## License
MIT
