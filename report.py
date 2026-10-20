
from datetime import datetime


def format_financial_report(
    ticker: str,
    stock_data: dict,
    news_data: dict,
) -> str:
    """Format stock data and news results into a readable report."""

    lines = [
        "=" * 60,
        f"FINANCIAL ANALYSIS REPORT: {ticker.upper()}",
        f"Generated at: {datetime.now().astimezone().strftime('%Y-%m-%d %H:%M %Z')}",
        "=" * 60,
        "",
        "1. STOCK MARKET DATA",
    ]

    if stock_data.get("error"):
        lines.append(f"Unable to retrieve stock data: {stock_data['error']}")
    else:
        
        lines.extend([
            f"Ticker: {stock_data.get('ticker', ticker.upper())}",
            f"Data date: {stock_data.get('date', 'Unavailable')}",
            f"Open: ₹{stock_data.get('open', 'N/A')}",
            f"High: ₹{stock_data.get('high', 'N/A')}",
            f"Low: ₹{stock_data.get('low', 'N/A')}",
            f"Close: ₹{stock_data.get('close', 'N/A')}",
            f"Previous Close: ₹{stock_data.get('previous_close', 'N/A')}",
            f"Daily Change: ₹{stock_data.get('change', 'N/A')}",
            f"Daily Change (%): {stock_data.get('change_percent', 'N/A')}%",
            f"Volume: {stock_data.get('volume', 'N/A')}",
        ])


    lines.extend(["", "2. RECENT FINANCIAL NEWS"])

    if news_data.get("error"):
        lines.append(f"Unable to retrieve news: {news_data['error']}")
    else:
        results = news_data.get("results", [])

        if not results:
            lines.append("No news results were returned.")
        else:
            for index, item in enumerate(results, start=1):
                lines.extend([
                    f"{index}. {item.get('title', 'Untitled')}",
                    f"   URL: {item.get('url', 'Unavailable')}",
                    f"   Summary: {item.get('content', 'No summary available')}",
                    "",
                ])

    lines.extend([
        "3. IMPORTANT LIMITATIONS",
        "- Market data and news may have different timestamps.",
        "- News summaries are not verified investment recommendations.",
        "- This report is informational, not a guarantee of future returns.",
        "=" * 60,
    ])

    return "\n".join(lines)


if __name__ == "__main__":
    # Small formatting test; no API call is required.
    sample_stock = {
        "ticker": "TCS.NS",
        "date": "2026-10-19",
        "open": 2458.0,
        "high": 2497.0,
        "low": 2432.1,
        "close": 2460.9,
        "volume": 8676373,
    }

    sample_news = {
        "results": [
            {
                "title": "Example financial news headline",
                "url": "https://example.com/news",
                "content": "This is sample text for testing report formatting.",
            }
        ]
    }

    print(format_financial_report("TCS.NS", sample_stock, sample_news))
