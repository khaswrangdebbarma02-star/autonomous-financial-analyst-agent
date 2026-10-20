
from langchain_core.tools import tool

from tools.stock_data import get_stock_data
from tools.news_search import search_financial_news


@tool
def stock_market_tool(ticker: str) -> dict:
    """Get recent prices and trading volume for a stock.
    Use Indian NSE ticker symbols such as RELIANCE.NS or TCS.NS.
    """
    return get_stock_data(ticker)


@tool
def financial_news_tool(query: str) -> dict:
    """Search for recent financial news about a company, stock,
    financial market, or economic topic.
    """
    return search_financial_news(query)


if __name__ == "__main__":
    print("Available financial tools:")
    for financial_tool in [stock_market_tool, financial_news_tool]:
        print(f"- {financial_tool.name}: {financial_tool.description}")

    print("\nTesting stock tool:")
    print(stock_market_tool.invoke({"ticker": "TCS.NS"}))

    print("\nTesting news tool:")
    print(financial_news_tool.invoke({"query": "TCS stock"}))
