import airflow

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

dag = DAG(
    dag_id = 'test',
    start_date = airflow.utils.dates.days_ago(14),
    schedule_interval=None,
)

download_launches = BashOperator(
    task_id = "download_launches",
    bash_command = "echo Hi",
    dag=dag,
)

def _get_hi():
    print('Hi python')

get_pictures=PythonOperator(
    task_id="get_pictures",
    python_callable=_get_hi,
    dag=dag,
)

download_launches >> get_pictures