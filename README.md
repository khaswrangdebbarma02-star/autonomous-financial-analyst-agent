# Autonomous Financial Analyst Agent

A Python-based financial analysis project that retrieves stock market data, searches recent financial news, and generates structured financial reports. It also includes an AI-powered financial analyst agent built with LangChain and OpenAI.

## Features

- **Stock Market Data:** Retrieves recent stock prices, previous closing prices, daily price changes, percentage changes, and trading volume using Yahoo Finance.
- **Financial News Search:** Searches for recent financial news using the Tavily Search API.
- **Automated Financial Reports:** Combines stock market data and news into structured, readable reports.
- **Report Saving:** Saves generated reports as Markdown files in the `reports/` directory.
- **AI Financial Analyst:** Uses LangChain and an OpenAI language model to coordinate financial tools and answer financial questions.
- **Automated Testing:** Uses pytest to test stock-data calculations and report formatting.

## Technologies Used

- Python
- LangChain
- OpenAI API
- Yahoo Finance (`yfinance`)
- Tavily Search API
- pandas
- pytest
- python-dotenv

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
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/khaswrangdebbarma02-star/autonomous-financial-analyst-agent.git
cd autonomous-financial-analyst-agent
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

Activate it on macOS or Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure API keys

This project uses OpenAI for AI-powered analysis and Tavily for financial news searches.

Create a `.env` file in the root directory of the project:

```text
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Get your API keys from:

- **OpenAI API:** https://platform.openai.com/api-keys
- **Tavily:** https://app.tavily.com/

Replace the placeholder values with your own API keys.

**Security note:** Never publish real API keys in your README, source code, screenshots, or public GitHub repository. Keep your `.env` file private. It is excluded from Git using `.gitignore`.

## Usage

### Generate a Financial Report

Run:

```bash
python generate_report.py
```

Enter a stock ticker when prompted. For example:

```text
TCS.NS
```

The program fetches available stock data, searches for financial news, generates a structured report, displays it in the terminal, and saves a Markdown copy in the `reports/` directory.

Other example Indian stock tickers include:

- `RELIANCE.NS` — Reliance Industries
- `INFY.NS` — Infosys
- `HDFCBANK.NS` — HDFC Bank

Market data availability depends on the data provider.

### Run the AI Financial Analyst Agent

Run:

```bash
python agent.py
```

You can then enter financial questions in the terminal. For example:

```text
Analyze TCS stock using recent market data and financial news.
```

Type `exit` to quit the application.

**Requirement:** The AI agent needs a valid OpenAI API key with available API quota. The financial news tool also requires a valid Tavily API key.

### Run the Automated Tests

Run:

```bash
python -m pytest -v
```

The current test suite covers stock ticker validation, invalid ticker handling, daily price-change calculations, and financial report formatting.

## Sample Report Contents

A generated report may include:

- Stock ticker and market-data date
- Opening, highest, lowest, and closing prices
- Previous closing price
- Daily price and percentage changes
- Trading volume
- Recent financial news and source links
- Analysis notes and limitations

The report includes information available from the configured data providers.

## Limitations

- Market data availability and timestamps depend on Yahoo Finance and the relevant exchange.
- News results may include irrelevant, incomplete, or inaccurate information.
- AI-generated analysis can make mistakes and should be independently verified.
- Live AI responses require available OpenAI API quota.
- This project does not guarantee stock-price predictions or investment returns.

## Future Improvements

- Interactive Streamlit dashboard
- Historical stock-price charts and technical indicators
- Improved news relevance filtering and date extraction
- Stock comparison and portfolio monitoring
- Additional automated tests
- More robust error handling and logging

## Disclaimer

This project is intended for educational and informational purposes only. It does not constitute financial, investment, or trading advice. Always verify market data independently and consult a qualified financial professional when appropriate.

## Author

**Khaswrang Debbarma**

GitHub: https://github.com/khaswrangdebbarma02-star

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
