'''
This is an example to demonstrate the functionality of the MCP server with Agno agent.
'''
import asyncio
from dotenv import load_dotenv
load_dotenv()

import os
os.environ["NO_PROXY"] = "localhost, 127.0.0.1"
os.environ["no_proxy"] = "localhost, 127.0.0.1"

import sys
# Add src to path to import our modules
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from agno.agent import Agent
from agno.tools.mcp import MCPTools
from agno.models.openai.responses import OpenAIResponses

import typer
app = typer.Typer()

async def run_agent(ticker: str) -> None:
    '''
    Run the financial analyst agent with the given message.
    The agent is connected with the tools from the MCP server stock_intelligence_cmp.
    Make sure that the MCP server is running before executing this script.
    In this example, this server is running on localhost port 8008 with streamable-http transport.
    '''
    
    message = f'''
        Provide a summary of the most recent stock performance for {ticker} in 2025.

        First provide a brief overview of the company's business.

        Then analyze the stock performance using data retrieved from the MCP server.
        
        Please include following key metrics:
            - Closing price changes of last 14 days, 
            - Analyst recommendations, 
            - Technical indicators such as RSI, TSI, and Williams %R.
        Format the response using markdown and include tables where appropriate.
        '''

    # Initialize and connect to the MCP server
    try:
        mcp_tools = MCPTools(
            url="http://localhost:8008/mcp",
            transport="streamable-http",
            timeout_seconds=60
            )
        await mcp_tools.connect()
    except Exception as e:
        print(f"Error connecting to MCP server: {e}")
        return

    try:
        agent = Agent(
            model=OpenAIResponses(id="gpt-4.1"),
            tools=[mcp_tools],
            description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
            instructions=['''Format your response using markdown and use tables to display data where possible.
                             Use the tools available ONLY to you to gather the necessary data to answer the user's query.
                             If no relevant information can be found over the tools, respond with "No relevant information found."'''],
            )
    
        # Run the agent
        await agent.aprint_response(message, markdown=True, stream=True)

    except Exception as e:
        print(f"Error while running the agent: {e}")
        return

    finally:
        # Always close the connection when done
        await mcp_tools.close()

@app.command()
def main(
    ticker: str = typer.Option(
        "SNOW", 
        help="Name or Symbol of like (APPL or MSFT) the stock that is to be analyzed."
        )
    ):
    '''
    Entry point for typer app command.
    '''
    asyncio.run(run_agent(ticker))

if __name__ == "__main__":
    app()
