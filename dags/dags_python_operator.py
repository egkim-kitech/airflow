import datetime
import pendulum

from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator
import random

with DAG(
    dag_id="dags_python_operator",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    def select_fruit():
        fruit = ['Apple', 'Banana', 'Cherry', 'Durian', 'Elderberry']
        random_fruit = random.choice(fruit)
        print(f"Today's fruit is {random_fruit}")

    def select_vegetable():
        vegetable = ['Asparagus', 'Broccoli', 'Cabbage', 'Daikon', 'Eggplant']
        random_vegetable = random.choice(vegetable)
        print(f"Today's vegetable is {random_vegetable}")

    py_t1 = PythonOperator(
        task_id="py_t1",
        python_callable=select_fruit,
    )    

    py_t2 = PythonOperator(
        task_id="py_t2",
        python_callable=select_vegetable,
    )

    py_t1 >> py_t2