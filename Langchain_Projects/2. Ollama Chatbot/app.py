from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

##prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to user queries"),
        ("user","question:{Question}")
    ]
)

def generate_response(question, temperature, max_tokens):
    llm = OllamaLLM(model = "gemma:2b")
    parser = StrOutputParser()
    chain = prompt|llm|parser
    response = chain.invoke({"Question": question})
    return response

st.title("Q&A Chatbot with Ollama")

st.sidebar.title("Settings")
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max_tokens", min_value=50, max_value=300, value=150)
st.sidebar.selectbox("Select Ollama model",["gemma:2b"])

st.write("Hi, How can I help you today?")
user_query = st.text_input("You:")

if user_query:
    response = generate_response(user_query, temperature, max_tokens)
    st.write(response)
else:
    st.write("Please enter user input")