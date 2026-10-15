import os
from dotenv import load_dotenv
load_dotenv()

from langchain_ollama import OllamaLLM
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

##Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system","You are an expert AI Assistant, Please responde to the question asked"),
    ("user","Question: {question}")
])

## Streamlit Interface
st.title("Langchain Demo with LLm")
input_text = st.text_input("What question you have in mind?")

##Ollama Llama2
llm = OllamaLLM(model = "gemma:2b")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))
