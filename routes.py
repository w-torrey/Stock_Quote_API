from fastapi import HTTPException, Query, APIRouter
import services

router = APIRouter()

@router.get("/")
def root():
    return "This is a stock quote API. use /quote/{ticker} to get the latest stock quote the provided stock ticker "


@router.get("/quote/{ticker}")
def get_quote(ticker: str):
    try:
        return services.quote_logic(ticker)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@router.get("/history/{ticker}")
def get_history(ticker: str, limit: int = Query(30, ge=1, le=100)):
    try:
        return services.history_logic(ticker, limit)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    

@router.get("/health")
def get_health():
    return services.health_logic()
