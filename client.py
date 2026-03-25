import os, requests
from dotenv import load_dotenv
from exceptions import ProviderUnavailableError, ProviderRateLimitError, ProviderResponseError, SymbolNotFoundError

load_dotenv()

api_key = os.getenv("API_KEY")
if not api_key:
    raise ValueError("Missing API_KEY")


def fetch_quote(ticker):
    url = f"https://www.alphavantage.co/query"
    params = {"function": "GLOBAL_QUOTE", "symbol": ticker, "apikey": api_key}
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        raise ProviderUnavailableError("Alpha Vantage timed out")
    except requests.exceptions.RequestException:
        raise ProviderUnavailableError("Alpha Vantage could not be reached")
    data = response.json()

    if "Note" in data:
        raise ProviderRateLimitError("Aplha Vantage has hit a rate limit")
    if "Error Message" in data:
        raise ProviderResponseError("Alpha Vantage response not provided")
    return data


def fetch_history(ticker):
    url = f"https://www.alphavantage.co/query"
    params = {"function": "TIME_SERIES_DAILY", "symbol": ticker, "apikey": api_key}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()
