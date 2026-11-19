from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a:int, b:int)-> int:
    """Add the numbers
    """
    return a+b

@mcp.tool()
def multiple(a:int,b:int) -> int:
    """ Multiply the numbers"""
    return a*b

#The transport "stdio" argument tells the server to:

#Use standard input and output (stdin and stdout) to receive and respond to tool function

if __name__ == "__main__":
    mcp.run(transport ="stdio")

    