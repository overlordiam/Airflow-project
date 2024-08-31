from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from dags.youtube_dags.tasks.ingest_data import ingest_data
from dags.youtube_dags.tasks.process_data import process_data


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
    dag_id = 'youtube_videos_analytics_dag',
    description = 'youtube data lifecylce',
    default_args=default_args,
    schedule_interval=None
)

run_ingestion = PythonOperator(
    task_id = 'fetch_video_info',
    python_callable=ingest_data,
    dag=dag,
)

run_process = PythonOperator(
    task_id = 'process_video_info',
    python_callable=process_data,
    dag=dag
)

run_ingestion >> run_process



