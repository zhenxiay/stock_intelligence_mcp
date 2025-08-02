import yfinance as yf
from ta.momentum import rsi
from utils.input_preprocessor import preprocess_rsi_input

'''
CreateTicker class to interact with yfinance for stock data retrieval.
The methods defined in this class are used as tools in the MCP server.'''

class CreateTicker():
    '''
    Create a yfinance ticker object for a given stock symbol.
    '''

    def __init__(self, stock: str):
        '''
        Initialize the ticker object with the stock symbol.
        '''
        self.ticker = yf.Ticker(stock)

    def fetch_closing(self):
        """
        Fetch closing price of the stock for the mcp tool from yfinance.
        """
        data = self.ticker.history(period="1d")
        latest_close = data['Close'].iloc[-1]

        return latest_close

    def get_recommendations_rsi(self, rsi_window):
        '''
        Calculate RSI and return recommendation based on RSI value.
        '''
        rsi_window = preprocess_rsi_input(rsi_window)

        df_input = self.ticker.history(period="1mo")

        rsi_series = rsi(
              close= df_input["Close"],
              window= rsi_window,
              fillna= False
              )
        rsi_index = rsi_series.iloc[-1]

        action = (
            'sell' if rsi_index > 70 else
            'buy' if rsi_index < 30 else
            'hold'
        )

        return {f"rsi_{rsi_window}": rsi_index, "recommendation": action}

    def get_recommendations_analysts(self):
        '''
        Get recommendations summary for the mcp tool from yfinance.
        '''
        return self.ticker.get_recommendations()

    def get_recent_news(self):
        '''
        Get recommendations summary for the mcp tool from yfinance.
        '''
        news=self.ticker.get_news(count=3,tab='press releases')

        result = [
        {
            "title": item["content"]["title"],
            "summary": item["content"]["summary"]
        }
        for item in news
        ]

        return result
    