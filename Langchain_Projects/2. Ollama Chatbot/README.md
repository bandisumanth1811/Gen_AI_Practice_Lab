# Q&A Chatbot with Ollama

A Streamlit chatbot built with LangChain that runs a local model (`gemma:2b`) through Ollama, so no API key is needed.

## Run
```bash
ollama pull gemma:2b
cd Langchain_Projects
pip install -r requirements.txt
streamlit run "2. Ollama Chatbot/app.py"
```
Ollama must be installed and running.
