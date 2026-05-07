# CoIn Market Data Tool

import yfinance as yf
import pandas as pd
from datetime import datetime

def get_market_data(ticker, period='1y'):
    """Fetch OHLCV data with metadata for Research/Backtesting agents."""
    data = yf.download(ticker, period=period)
    info = yf.Ticker(ticker).info
    return {
        "ticker": ticker,
        "data": data.to_dict(),
        "info": info,
        "timestamp": datetime.now().isoformat()
    }

if __name__ == "__main__":
    print(get_market_data('SPY'))