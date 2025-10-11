
'''
This is the entrypoint to the Stock Intelligence MCP server.
'''
from mcp.server.fastmcp import FastMCP
import typer
from stock_intelligence_mcp.ticker.ticker import CreateTicker

app = typer.Typer()

@app.command()
def main(
    name: str = typer.Option(
                    "StockIntelligence", 
                    help="Name of the MCP server."
                            ),
    port: int = typer.Option(
                    8000,
                    help="Port of the MCP server.",
                    show_default=True
                    ),
    transport: str = typer.Option(
                    "sse",
                    help="Transport layer. Choose between stdio, sse or streamable-http",
                    show_default=True
                    )
    ):
    """
    This is the entrypoint to the app.
    """
    mcp = FastMCP(
        name=name,
        port=port
        )

    @mcp.tool()
    def get_closing_stock_price(stock) -> dict:
        """
        Get the closing price of the stock asked in the question.
        """
        ticker = CreateTicker(stock)
        return ticker.fetch_closing()

    @mcp.tool()
    def get_14d_closing_stock_price(stock):
        """
        Get the last 14 days closing price of the stock asked in the question.
        """
        ticker = CreateTicker(stock)
        return ticker.fetch_14d_closing()

    @mcp.tool()
    def technical_analysis_rsi(stock, rsi_window) -> dict:
        """
        Get the recommendations based on the calculated Relative Strength Index (RSI).
        """
        ticker = CreateTicker(stock)
        return ticker.get_recommendations_rsi(rsi_window)

    @mcp.tool()
    def get_sell_buy_advice(stock) -> dict:
        """
        Get recommendations summary (buy, sell or hold) from yfinance.
        """
        ticker = CreateTicker(stock)
        return ticker.get_recommendations_analysts()

    @mcp.tool()
    def get_recent_stock_news(stock) -> dict:
        """
        Get recent news of the stock from yfinance.
        """
        ticker = CreateTicker(stock)
        return ticker.get_recent_news()

    @mcp.resource(uri="resource://server_prompt", 
                  mime_type="application/json",
                  description="Server specific prompt to guide the agent to interact with the server.")
    def get_prompt():
        """
        Resource for explaining the technical indicator RSI.
        """
        return {
            "prompt": (
                "You are a financial expert. You have access to tools from this server. "
                "Use these tools to answer questions about stock prices, trends, and recommendations. "
                "Provide clear and concise answers based on the data retrieved from the tools."
                "You also have access to resources that explains specific technical indicators. "
                "Use them to enhance your answers when relevant."
                "If the resource contains a markdown file, try to fetch its content to answer the question."
            ),
            "annotations": {
                "audience": ["assistant"],
                "priority": 1.0,
            }
        }
    
    @mcp.resource(uri="resource://RSI", 
                  mime_type="application/json",
                  description="Explanation of the technical indicator RSI.")
    def explain_rsi():
        """
        Resource for explaining the technical indicator RSI.
        """
        return {
            "uri": "file:///resources/RSI.md",
            "annotations": {
            "audience": ["assistant"],
            "priority": 0.8,
            }
        }
    
    @mcp.resource(uri="resource://RSI_read", 
                  mime_type="text/markdown",
                  description="Read and explain the technical indicator RSI.")
    async def read_rsi():
              """
              Reads the RSI.md file and returns its content.
              """
              import aiofiles
              try:
                  async with aiofiles.open("resources/RSI.md", mode="r") as f:
                      content = await f.read()
                      return content
              except FileNotFoundError:
                  return "Markdown file not found."
    
    mcp.run(transport)

if __name__ == "__main__":
    app()
