# src/main.py
import os
import logging
from dotenv import load_dotenv
from extractor.stock_fetcher import fetch_intraday_stock_data
from uploader.s3_uploader import upload_dataframe_to_s3

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
load_dotenv()

def main():
    symbol = os.getenv("SYMBOL", "TSLA")
    interval = os.getenv("INTERVAL", "5min")
    api_key = os.getenv("API_KEY")
    bucket = os.getenv("AWS_BUCKET_NAME")
    key = f"stock_data/{symbol}_stock_data.csv"

    try:
        df = fetch_intraday_stock_data(symbol, interval, api_key)
        upload_dataframe_to_s3(df, bucket, key)
    except Exception as e:
        logging.error(f"Pipeline failed: {e}")

if __name__ == "__main__":
    main()
