# Autonomous Financial Analyst Agent

A Python-based financial analysis project that collects stock market data, searches recent financial news, and generates structured financial reports.

## Features

- **Stock Market Data:** Retrieves recent stock prices, previous close, daily price changes, and trading volume using yfinance.
- **Financial News Search:** Searches for recent financial news using the Tavily API.
- **Automated Reports:** Combines market data and news into a readable report.
- **Report Saving:** Saves generated reports as Markdown files in the `reports/` folder.
- **AI Agent:** Uses LangChain and an OpenAI language model to coordinate financial tools.
- **Automated Testing:** Uses pytest to verify stock-data calculations and report formatting.

## Technologies

Python · LangChain · OpenAI API · yfinance · Tavily · pandas · pytest

## Project Structure

```text
autonomous-financial-analyst-agent/
├── tools/
│   ├── __init__.py
│   ├── stock_data.py
│   ├── news_search.py
│   └── agent_tools.py
├── tests/
│   ├── test_stock_data.py
│   └── test_report.py
├── reports/
├── agent.py
├── generate_report.py
├── report.py
├── main.py
├── openai_api_check.py
├── requirements.txt
└── .gitignore
```

## Installation

### 1. Clone the repository

Replace the placeholder with your actual GitHub repository URL.

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd autonomous-financial-analyst-agent
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure API keys

Create a `.env` file in the project root:

```text
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Replace the placeholders with your own API keys. Never upload `.env` or expose your keys publicly.

## Usage

### Generate a financial report

```bash
python generate_report.py
```

Enter a stock ticker, for example:

```text
TCS.NS
```

The script fetches available stock data, searches financial news, displays the report, and saves a Markdown copy in `reports/`.

### Run the AI agent

```bash
python agent.py
```

The AI agent requires a valid OpenAI API key with available API quota.

### Run automated tests

```bash
python -m pytest -v
```

## Limitations

- Market data availability depends on the data provider.
- News search results may contain irrelevant or incomplete information.
- AI analysis requires OpenAI API access and available quota.
- This project does not guarantee stock-price predictions or investment returns.

## Future Improvements

- Historical stock-price charts.
- Improved news filtering and date extraction.
- Interactive dashboard.
- Portfolio monitoring.
- Additional automated tests.

## Disclaimer

This project is for educational and informational purposes only. Verify financial data independently before making investment decisions.
