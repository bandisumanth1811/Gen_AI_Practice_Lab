from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes
import os 
from dotenv import load_dotenv
load_dotenv()
groq_api_key = os.getenv('GROQ_API_KEY')
llm = ChatGroq(model="openai/gpt-oss-20b", groq_api_key = groq_api_key)

general_template = "Translate the following into {language}"
prompt = ChatPromptTemplate.from_messages([
    ("system",general_template),
    ("user","{text}")
])

parser = StrOutputParser()

chain = prompt|llm|parser

app = FastAPI(title = "langchain_server",
              version = "1.0",
              description="A Simple API server using runnable langchain interfaces")

add_routes(app, chain, path = "/chain")

if __name__ =="__main__":
    import uvicorn
    uvicorn.run(app, host = "localhost", port=8000)

