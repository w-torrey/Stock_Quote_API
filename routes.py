from fastapi import FastAPI, HTTPException, Query
import services

app = FastAPI()

@app.get("/")
def root():
    return ("This is a stock quote API. use /quote/{ticker} to get the latest stock quote the provided stock ticker ")

# @app.get("/health")

@app.get("/quote/{ticker}")
def get_quote(ticker):
    return services.quote_logic(ticker)

@app.get("/history/{ticker}")
def get_history(ticker: str, range: int = Query(30, ge=1, le=100)):
    return services.history_logic(ticker, range)
