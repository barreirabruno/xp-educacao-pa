from datetime import datetime
from airflow import DAG

from airflow.operators.python import PythonOperator

def _main():
  print("HELLO NEW DAG")

default_args = {
    'start_date': datetime(2022, 12, 1)
}

with DAG('process_donations_by_sponsor_id_salic', schedule_interval='@daily',
        default_args=default_args,
        catchup=False) as dag:

    request_salic_api = PythonOperator(
            task_id="process_donations_by_sponsor_id",
            python_callable=_main
    )

request_salic_api
