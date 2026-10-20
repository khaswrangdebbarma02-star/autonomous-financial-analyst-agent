
from datetime import datetime
from pathlib import Path

from tools.stock_data import get_stock_data
from tools.news_search import search_financial_news
from report import format_financial_report


REPORTS_DIR = Path(__file__).resolve().parent / "reports"


def generate_report(ticker: str) -> str:
    """Fetch stock data and news, generate a report, and save it."""

    ticker = ticker.strip().upper()

    if not ticker:
        return "Please enter a valid stock ticker."

    print(f"\nFetching stock data for {ticker}...")
    stock_data = get_stock_data(ticker)

    print(f"Searching for financial news about {ticker}...")
    news_data = search_financial_news(f"{ticker} stock financial news")

    report = format_financial_report(ticker, stock_data, news_data)

    # Ensure the reports folder exists.
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    # Create a unique filename for this report.
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    safe_ticker = ticker.replace(".", "_").replace("/", "_")
    filename = f"{safe_ticker}_{timestamp}.md"
    report_path = REPORTS_DIR / filename

    # Save the report.
    report_path.write_text(report, encoding="utf-8")

    print(f"\nReport saved successfully: {report_path}")

    return report


if __name__ == "__main__":
    ticker = input("Enter stock ticker (e.g., TCS.NS): ").strip()
    report = generate_report(ticker)
    print("\n" + report)
