from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
async def get_weather(location:str) -> str:
    """Get the weather location"""
    return "It's always raining in New York City"


if __name__ == "__main__":
    mcp.run(transport="streamable-http")

# both weather and math server running, but at the end of the day the client has to interact with both server and host right

