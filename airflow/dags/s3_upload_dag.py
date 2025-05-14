from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import subprocess

def run_stock_upload():
    subprocess.run(["python", "/workspace/src/main.py"], check=True)

default_args = {
    "owner": "you",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="s3_stock_data_upload",
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:

    upload_task = PythonOperator(
        task_id="upload_stock_data_to_s3",
        python_callable=run_stock_upload,
    )
