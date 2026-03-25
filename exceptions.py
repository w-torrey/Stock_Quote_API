class StockAPIError(Exception):
    pass
class ProviderError(StockAPIError):
    pass
class ProviderUnavailableError(ProviderError):
    pass

class ProviderRateLimitError(ProviderError):
    pass

class ProviderResponseError(ProviderError):
    pass

class SymbolNotFoundError(StockAPIError):
    pass

