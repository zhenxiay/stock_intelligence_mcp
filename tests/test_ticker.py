import pytest
from unittest.mock import patch, MagicMock
from stock_intelligence_mcp.ticker.ticker import CreateTicker
import pandas as pd
import json

@pytest.fixture
def mock_ticker():
    """Mocks the yfinance Ticker object."""
    with patch('yfinance.Ticker') as mock_yf_ticker:
        mock_instance = MagicMock()
        # Mock the history() method to return a dummy DataFrame, as it's called by the function.
        mock_instance.history.return_value = pd.DataFrame({'Close': [100, 110, 120, 130]})
        mock_yf_ticker.return_value = mock_instance
        yield mock_instance

def test_get_recommendations_rsi_returns_valid_dict(mock_ticker):
    """
    Tests that get_recommendations_rsi returns a dictionary with the correct structure.
    """
    # Arrange
    rsi_window = 14
    # The function under test calls `rsi` from `ta.momentum`
    with patch('stock_intelligence_mcp.ticker.ticker.rsi') as mock_rsi:
        # Mock the return of the rsi function to be a pandas Series-like object
        # where the last item can be accessed via .iloc[-1]
        mock_series = MagicMock()
        mock_series.iloc.__getitem__.return_value = 50  # A neutral RSI value
        mock_rsi.return_value = mock_series

        ticker = CreateTicker("AAPL")

        # Act
        result = ticker.get_recommendations_rsi(rsi_window)

        # Assert
        assert result is not None
        assert isinstance(json.loads(result), dict)
        assert "recommendation" in json.loads(result)["content"]

def test_get_company_info():
    """
    Test that get_company_info function returns the correct output as expected.
    """
    # Create ticker
    ticker = CreateTicker("SNOW")
    
    # Get result
    result = ticker.get_company_info()
    
    # Assert
    assert result is not None
