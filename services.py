import client, time
from datetime import datetime, timezone


start_time = time.time()


def quote_logic(ticker):
    ticker = ticker_validation(ticker)
    raw = client.fetch_quote(ticker)
    quote = raw.get("Global Quote", {})
    return {
        "symbol": quote.get("01. symbol"),
        "price": quote.get("05. price"),
        "volume": quote.get("06. volume"),
        "latest_trading_day": quote.get("07. latest trading day"),
    }


def history_logic(ticker, days=30):
    ticker = ticker_validation(ticker)
    day_validation(days)
    raw = client.fetch_history(ticker)
    history = raw.get("Time Series (Daily)", {})
    sorted_dates = sorted(history.keys(), reverse=True)
    result = []
    for date in sorted_dates[:days]:
        day_data = history[date]
        result.append(
            {
                "symbol": ticker,
                "date": date,
                "open": day_data.get("1. open"),
                "high": day_data.get("2. high"),
                "low": day_data.get("3. low"),
                "close": day_data.get("4. close"),
                "volume": day_data.get("5. volume"),
            }
        )
    return result

def health_logic():
    now = time.time()
    uptime = now - start_time
    return {
        'status': 'ok',
        'uptime': uptime,
        'timestamp': datetime.now(timezone.utc).isoformat()
        }

def ticker_validation(ticker):
    if not isinstance(ticker, str):
        raise ValueError("Please return string")
    if not ticker:
        raise ValueError("Please return a ticker")
    if not 1 <= len(ticker) <= 5:
        raise ValueError("Please return a valid ticker less than 5 characters")
    if not ticker.isalpha():
        raise ValueError("Please return a valid ticker with only letters")
    return ticker.upper()
    
def day_validation(days):
    if not isinstance(days, int):
        raise ValueError("Please return an integer for range")
    if not 1 <= days <= 100:
        raise ValueError("Please return a valid range between 1 and 100")
    return days
