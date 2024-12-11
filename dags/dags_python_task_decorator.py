from airflow.models.dag import DAG
import pendulum
from airflow.decorators import task

with DAG(
    dag_id="dags_python_task_decorator",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:

    @task(task_id="python_task_1")
    def print_something(something):
        print(something)

    python_task_1 = print_something("task_decorator 실행")