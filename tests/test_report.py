
from report import format_financial_report


def test_report_contains_stock_data():
    stock_data = {
        "ticker": "TCS.NS",
        "date": "2026-10-19",
        "open": 100.0,
        "high": 110.0,
        "low": 95.0,
        "close": 105.0,
        "previous_close": 100.0,
        "change": 5.0,
        "change_percent": 5.0,
        "volume": 1500,
    }

    news_data = {"results": []}

    report = format_financial_report(
        "TCS.NS", stock_data, news_data
    )

    assert "FINANCIAL ANALYSIS REPORT: TCS.NS" in report
    assert "TCS.NS" in report
    assert "105.0" in report
    assert "RECENT FINANCIAL NEWS" in report


def test_report_handles_stock_error():
    stock_data = {"error": "No market data found."}
    news_data = {"results": []}

    report = format_financial_report(
        "INVALID", stock_data, news_data
    )

    assert "No market data found." in report
    assert "RECENT FINANCIAL NEWS" in report
