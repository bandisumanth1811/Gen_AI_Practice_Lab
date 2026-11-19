from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(model="openai/gpt-oss-20b", groq_api_key=groq_api_key)

import asyncio

async def main():
    client = MultiServerMCPClient(
        {
            "math":{
                "command":"python",
                "args":["mathserver.py"], #ensure tp enter the absolute file location 
                "transport":"stdio"
            },
            "weather":{
                "url": "http://127.0.0.1:8000/mcp",
                "transport":"streamable-http"
            }
        }
    )

    tools = await client.get_tools()

    agent = create_react_agent(llm , tools)

    math_response = await agent.ainvoke(
        {"messages": [ {"role":"user", "content": "what's (3+5)*12"}]}
    )

    print("Math response:", math_response['messages'][-1].content)

    # 4. Test the weather tool (handled by HTTP server running in your other terminal)
    weather_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what is the weather in New York?"}]}
    )
    print("Weather response:", weather_response['messages'][-1].content)

asyncio.run(main())