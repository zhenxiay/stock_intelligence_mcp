
'''
CreateTicker class to interact with yfinance for stock data retrieval.
The methods defined in this class are used as tools in the MCP server.
'''

import yfinance as yf
from ta.momentum import rsi, tsi, williams_r
from stock_intelligence_mcp.utils.input_preprocessor import preprocess_rsi_input
from stock_intelligence_mcp.utils.output_preprocessor import json_output

class CreateTicker():
    '''
    Create a yfinance ticker object for a given stock symbol.
    '''

    def __init__(self, stock: str):
        '''
        Initialize the ticker object with the stock symbol.
        '''
        self.ticker = yf.Ticker(stock)

    def get_company_info(self):
        '''
        Get company information from yfinance.
        '''
        info = self.ticker.info['longBusinessSummary']

        return json_output({"company_info": info})
    
    def fetch_closing(self):
        """
        Fetch closing price of the stock for the mcp tool from yfinance.
        """
        data = self.ticker.history(period="1d")
        latest_close = data['Close'].iloc[-1]

        return latest_close

    def fetch_14d_closing(self):
        """
        Fetch last 14 days closing price of the stock for the mcp tool from yfinance.
        """
        data = self.ticker.history(period="14d")

        return data[["Close"]].to_markdown()

    def get_recommendations_rsi(self, rsi_window):
        '''
        Calculate RSI and return recommendation based on RSI value.
        '''
        rsi_window = preprocess_rsi_input(rsi_window)

        df_input = self.ticker.history(period="1mo")

        rsi_series = rsi(
              close=df_input["Close"],
              window=rsi_window,
              fillna=False
              )
        rsi_index = rsi_series.iloc[-1]

        action = (
            'sell' if rsi_index > 70 else
            'buy' if rsi_index < 30 else
            'hold'
        )

        output = {f"rsi_{rsi_window}": rsi_index, "recommendation": action}

        return json_output(output)
    
    def get_recommendations_tsi(self):
        '''
        Calculate TSI (True Strength Index) and return recommendation based on TSI value.
        '''

        df_input = self.ticker.history(period="1mo")

        tsi_series = tsi(
              close=df_input["Close"],
              fillna=False
              )
        tsi_index = tsi_series.iloc[-1]

        output = {f"tsi_index": tsi_index}

        return json_output(output)
    
    def get_recommendations_williams_r(self):
        '''
        Calculate Williams %R and return recommendation based on Williams %R value.
        '''
        df_input = self.ticker.history(period="1mo")

        williams_r_series = williams_r(
            high=df_input["High"],
            low=df_input["Low"],
            close=df_input["Close"],
            fillna=False
        )

        williams_r_index = williams_r_series.iloc[-1]

        action = (
            'sell' if williams_r_index > -20 else
            'buy' if williams_r_index < -80 else
            'hold'
        )

        output = {f"williams_r": williams_r_index, "recommendation": action}

        return json_output(output)

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

        return json_output(result)
