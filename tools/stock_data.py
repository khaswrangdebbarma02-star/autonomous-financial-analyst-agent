
import yfinance as yf


def get_stock_data(ticker: str) -> dict:
    """Fetch recent stock prices and calculate the latest daily change."""
    ticker = ticker.strip().upper()

    if not ticker:
        return {"error": "Please enter a stock ticker."}

    try:
        stock = yf.Ticker(ticker)
        history = stock.history(period="5d")

        if history.empty:
            return {
                "error": f"No market data found for {ticker}. "
                "Check the ticker symbol and try again."
            }

        latest = history.iloc[-1]
        previous_close = (
            float(history.iloc[-2]["Close"])
            if len(history) >= 2
            else None
        )

        close = float(latest["Close"])

        if previous_close is not None and previous_close != 0:
            change = close - previous_close
            change_percent = (change / previous_close) * 100
        else:
            change = None
            change_percent = None

        return {
            "ticker": ticker,
            "date": str(history.index[-1].date()),
            "open": round(float(latest["Open"]), 2),
            "high": round(float(latest["High"]), 2),
            "low": round(float(latest["Low"]), 2),
            "close": round(close, 2),
            "previous_close": (
                round(previous_close, 2)
                if previous_close is not None else None
            ),
            "change": round(change, 2) if change is not None else None,
            "change_percent": (
                round(change_percent, 2)
                if change_percent is not None else None
            ),
            "volume": int(latest["Volume"]),
        }

    except Exception as exc:
        return {"error": f"Unable to fetch data for {ticker}: {exc}"}


if __name__ == "__main__":
    ticker = input("Enter stock ticker (e.g., TCS.NS): ")
    print(get_stock_data(ticker))
