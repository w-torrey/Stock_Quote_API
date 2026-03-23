import os, requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
if not api_key:
    raise ValueError("Missing API_KEY")


def fetch_quote(ticker):
    url = f"https://www.alphavantage.co/query"
    params = {"function": "GLOBAL_QUOTE", "symbol": ticker, "apikey": api_key}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


def fetch_history(ticker):
    url = f"https://www.alphavantage.co/query"
    params = {"function": "TIME_SERIES_DAILY", "symbol": ticker, "apikey": api_key}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()
