from __future__ import annotations

import datetime

import pendulum

from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="dags_bash_select_fruit",
    schedule="10 0 * * 6#1",
    start_date=pendulum.datetime(2024, 1, 1, tz="UTC"),
    catchup=False,
) as dag:
    # make empthy operator
    t1_APPLE = BashOperator(task_id="t1_APPLE", bash_command="/opt/airflow/plugins/shell/select_fruit.sh APPLE")
    t2_BANANA = BashOperator(task_id="t2_BANANA", bash_command="/opt/airflow/plugins/shell/select_fruit.sh BANANA")

    t1_APPLE >> t2_BANANA