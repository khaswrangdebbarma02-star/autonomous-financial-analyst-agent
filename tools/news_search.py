
import os
from datetime import date, timedelta

from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()


def search_financial_news(query: str) -> dict:
    """Search for recent financial news and filter poor-quality results."""
    api_key = os.getenv("TAVILY_API_KEY")

    if not api_key:
        return {"error": "TAVILY_API_KEY is missing from .env."}

    try:
        client = TavilyClient(api_key=api_key)

        response = client.search(
            query=f"{query} company stock market financial news",
            topic="news",
            days=30,
            max_results=10,
            search_depth="advanced",
        )

        results = []

        for item in response.get("results", []):
            title = item.get("title", "").strip()
            url = item.get("url", "").strip()
            content = item.get("content", "").strip()

            # Skip incomplete results.
            if not title or not url or not content:
                continue

            # Skip pages containing obvious broken template placeholders.
            if "{{" in title or "{{" in content:
                continue

            results.append({
                "title": title,
                "url": url,
                "content": content,
            })

        return {
            "query": query,
            "search_period_days": 30,
            "results": results,
            "message": (
                "No suitable results found in the last 30 days."
                if not results else None
            ),
        }

    except Exception as exc:
        return {"error": f"News search failed: {exc}"}


if __name__ == "__main__":
    query = input("Enter a company or financial topic: ").strip()

    if query:
        result = search_financial_news(query)
        for item in result.get("results", []):
            print(f"\nTitle: {item['title']}")
            print(f"URL: {item['url']}")
            print(f"Summary: {item['content'][:500]}")
        if result.get("error"):
            print(result["error"])
        elif not result.get("results"):
            print(result.get("message", "No suitable results found."))
