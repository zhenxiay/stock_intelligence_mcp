
'''
This is the entrypoint to the Stock Intelligence MCP server.
'''
from mcp.server.fastmcp import FastMCP
import typer
from ticker.ticker import CreateTicker

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
    def get_14d_closing_stock_price(stock) -> markdown:
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

    mcp.run(transport)

if __name__ == "__main__":
    app()
