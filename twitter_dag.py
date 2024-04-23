from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from twitter-etl import run_twitter_etl

default_arg = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime[2020, 11, 8],
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'twitter_dag',
    default_arg=default_arg,
    description='My first etl code'
)

# Python operator to run this DAG
run_etl = PythonOperator(
    task_id='complete_twitter_etl',  # anything you want
    python_callable=run_twitter_etl,  # function
    dag=dag,
)

run_etl