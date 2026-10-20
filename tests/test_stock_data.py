
from unittest.mock import patch

import pandas as pd

from tools.stock_data import get_stock_data


def test_empty_ticker():
    result = get_stock_data("")

    assert result == {"error": "Please enter a stock ticker."}


@patch("tools.stock_data.yf.Ticker")
def test_invalid_ticker(mock_ticker):
    mock_stock = mock_ticker.return_value
    mock_stock.history.return_value = pd.DataFrame()

    result = get_stock_data("INVALID")

    assert "error" in result
    assert "No market data found" in result["error"]


@patch("tools.stock_data.yf.Ticker")
def test_price_change_calculation(mock_ticker):
    mock_stock = mock_ticker.return_value

    history = pd.DataFrame(
        {
            "Open": [100.0, 104.0],
            "High": [105.0, 110.0],
            "Low": [98.0, 103.0],
            "Close": [100.0, 105.0],
            "Volume": [1000, 1500],
        },
        index=pd.to_datetime([
            "2026-10-16",
            "2026-10-19",
        ]),
    )

    mock_stock.history.return_value = history

    result = get_stock_data("TEST.NS")

    assert result["ticker"] == "TEST.NS"
    assert result["previous_close"] == 100.0
    assert result["close"] == 105.0
    assert result["change"] == 5.0
    assert result["change_percent"] == 5.0
    assert result["volume"] == 1500
