import streamlit as st
import groq
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

import os
from dotenv import load_dotenv
load_dotenv()

#Langsmith_Tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Q&A Chatbot with GROQ"

#groq_api_key = os.getenv('GROQ_API_KEY')
#llm = ChatGroq(model = "", groq_api_key = groq_api_key)

#Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are an expert helpful AI Assitant. Please response to the user queries"),
        ("user","Question : {question}")
    ])

def generate_response(question, api_key, engine, temperature, max_tokens):
    llm = ChatGroq(model=engine, groq_api_key = api_key, temperature= temperature, max_tokens=max_tokens)
    output_parser = StrOutputParser()
    chain = prompt|llm|output_parser
    answer = chain.invoke({"question":question })
    return answer

#Title of the APP
st.title("Enhanced Q&A Chatbot with GROQ")

##Side bar of the dashboard
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your GROQ API Key:", type = "password")
models = {"OpenAI GPT-OSS 120B (Advanced Reasoning)": "openai/gpt-oss-120b",
    "OpenAI GPT-OSS 20B (Fast)": "openai/gpt-oss-20b",
    "Qwen 3.8 27B (Reasoning & Vision)": "qwen/qwen3.8-27b",
    "MiniMax M2.7 (Advanced)": "minimaxai/minimax-m2.7",
    "GPT-OSS Safeguard 20B (Safety)": "openai/gpt-oss-safeguard-20b"}

selected_box = st.sidebar.selectbox("Select groq model", list(models.keys()))

#drop down to model selection
engine = models[selected_box]

temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

#Main interface for user input
st.write("How can I help you today!! Do you have any questions in your mind?")
user_input = st.text_input("You:")

if user_input and api_key:
    response = generate_response(user_input, api_key, engine, temperature, max_tokens)
    st.write(response)
elif user_input:
    st.write("Please enter valid Groq API Key in the sidebar")
else:
    st.write("Please provide user input")