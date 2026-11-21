# Q&A Chatbot with Groq

A Streamlit chatbot built with LangChain and Groq. Pick a Groq model, set temperature and max tokens in the sidebar, and ask questions. LangSmith tracking is enabled through `LANGCHAIN_API_KEY`.

## Run
```bash
cd Langchain_Projects
pip install -r requirements.txt
streamlit run "1. Q&A Chatbot/app.py"
```
Enter your Groq API key in the sidebar. For LangSmith tracing, copy `.env.example` to `.env` and set `LANGCHAIN_API_KEY`.
