# src/extractor/stock_fetcher.py
import requests
import pandas as pd
import logging

def fetch_intraday_stock_data(symbol: str, interval: str, api_key: str) -> pd.DataFrame:
    url = (
        f"https://www.alphavantage.co/query"
        f"?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval={interval}&apikey={api_key}"
    )
    logging.info(f"Requesting stock data from API for symbol: {symbol}")
    response = requests.get(url)
    data = response.json()

    key = f"Time Series ({interval})"
    if key in data:
        df = pd.DataFrame.from_dict(data[key], orient="index")
        df.columns = ["Open", "High", "Low", "Close", "Volume"]
        df.index = pd.to_datetime(df.index)
        return df
    else:
        raise ValueError("Invalid API response: " + str(data))
