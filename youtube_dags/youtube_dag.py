from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from utils import youtube_etl


default_args = {
    'owner': 'suhaas',
    'depends_on_past': False,
    'start_date': datetime(2020, 11, 8),
    'email': ['footballandgermany@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    dag_id = 'youtube_dag',
    description = 'youtube data lifecylce',
    default_args=default_args,
    schedule_interval=timedelta(days=1)
)

run_etl = PythonOperator(
    task_id = 'fetch_youtube_comments',
    python_callable=youtube_etl,
    dag=dag,
)