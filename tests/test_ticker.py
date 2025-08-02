import pytest
from unittest.mock import patch, MagicMock
from src.ticker.ticker import CreateTicker

@pytest.fixture
def mock_ticker():
    """Mocks the yfinance Ticker object."""
    with patch('yfinance.Ticker') as mock_yf_ticker:
        mock_instance = MagicMock()
        mock_yf_ticker.return_value = mock_instance
        yield mock_instance

@pytest.mark.parametrize("rsi_value, expected_action", [
    (80, 'sell'),
    (20, 'buy'),
    (50, 'hold'),
])
def test_get_recommendations_rsi(mock_ticker, rsi_value, expected_action):
    """Tests the get_recommendations_rsi function with different RSI values."""
    # Arrange
    with patch('src.ticker.ticker.rsi') as mock_rsi:
        mock_rsi.return_value.iloc = [-1]
        mock_rsi.return_value.iloc[-1] = rsi_value

        ticker = CreateTicker("AAPL")

        # Act
        result = ticker.get_recommendations_rsi(14)

        # Assert
        assert result["recommendation"] == expected_action
