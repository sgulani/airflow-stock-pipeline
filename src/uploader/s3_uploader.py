import boto3
import os
import logging
from io import StringIO
import pandas as pd
from botocore.exceptions import BotoCoreError, ClientError

def upload_dataframe_to_s3(df: pd.DataFrame, bucket: str, key: str):
    try:
        # Create AWS session using environment variables
        session = boto3.Session(
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
            region_name=os.getenv("AWS_DEFAULT_REGION")
        )

        # 🧪 DEBUG: Show which credentials are actually used
        #creds = session.get_credentials().get_frozen_credentials()
        #logging.info(f"🧪 AWS_ACCESS_KEY_ID used: {creds.access_key}")
        #logging.info(f"🧪 AWS_SECRET_ACCESS_KEY used: {creds.secret_key[:4]}...(shortened)")
        #logging.info(f"🧪 AWS_DEFAULT_REGION used: {session.region_name}")

        # Convert DataFrame to CSV in memory
        csv_buffer = StringIO()
        df.to_csv(csv_buffer)

        # Upload to S3
        s3 = session.client("s3")
        s3.put_object(Bucket=bucket, Key=key, Body=csv_buffer.getvalue())
        logging.info(f"✅ Upload successful to s3://{bucket}/{key}")
    except (BotoCoreError, ClientError) as e:
        logging.error(f"❌ Error during upload to S3: {e}")
        raise
