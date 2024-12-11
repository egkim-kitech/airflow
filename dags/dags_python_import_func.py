from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from common.common_func import get_sftp

with DAG(
    dag_id = 'python_import_func',
    schedule="0 0 0 0 0",
    start_date=datetime(2023, 1, 1,tz="Asia/Seoul"),
    catchup=False
) as dag:


    task_get_sftp = PythonOperator(
        task_id='task_get_sftp',
        python_callable=get_sftp
    )

    task_get_sftp