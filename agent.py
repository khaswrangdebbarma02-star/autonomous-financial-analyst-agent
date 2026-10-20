
import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

from tools.agent_tools import (
    stock_market_tool,
    financial_news_tool,
)

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError(
        "OPENAI_API_KEY is missing. Check your .env file."
    )

model = ChatOpenAI(
    model=os.getenv("OPENAI_MODEL", "gpt-5.5"),
    api_key=api_key,
)

agent = create_agent(
    model=model,
    tools=[
        stock_market_tool,
        financial_news_tool,
    ],
    system_prompt="""
    You are an autonomous financial analyst assistant.

    Your responsibilities:
    1. Understand the user's financial question.
    2. Use the stock tool when current or recent stock prices are needed.
    3. Use the financial news tool when news or market context is needed.
    4. Explain findings clearly and distinguish facts from opinions.
    5. Mention relevant dates and provide source URLs when available.
    6. Never invent prices, news, or financial data.
    7. Do not present your analysis as a guaranteed prediction
       or personalized investment advice.
    """,
)


if __name__ == "__main__":
    print("Financial Analyst Agent")
    print("Type 'exit' to quit.\n")

    while True:
        question = input("You: ").strip()

        if question.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        if not question:
            continue

        try:
            response = agent.invoke({
                "messages": [
                    {"role": "user", "content": question}
                ]
            })

            print("\nAnalyst:")
            print(response["messages"][-1].content)
            print()

        except Exception as exc:
            print(f"\nAgent error: {exc}\n")
