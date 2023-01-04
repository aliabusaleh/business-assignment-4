
from datetime import datetime, timedelta
import logging

from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.contrib.sensors.file_sensor import FileSensor

log = logging.getLogger(__name__)

default_args = {
    'dag_id': 'process_web_log',
    'schedule_interval': '@daily',
    'start_date': datetime(2022, 12, 15),
    'catchup': False,
    'tags': ['Assigment']
}

dag = DAG('process_web_log',
          default_args=default_args,
          catchup=False)

scanForLog = FileSensor(
   task_id='scan_for_log',
   filepath='/opt/airflow/dags/the_log/log.txt',
   fs_conn_id='default',
   dag=dag)

extract_logs = BashOperator(
    task_id='extract_data',
    bash_command="grep -o '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}' /opt/airflow/dags/the_log/log.txt > /opt/airflow/dags/the_log/extracted_data.txt",
    dag=dag)

filter_logs = BashOperator(
    task_id='transform_data',
    bash_command="awk '!/198.46.149.143/' /opt/airflow/dags/the_log/extracted_data.txt > /opt/airflow/dags/the_log/transformed_data.txt",
    dag=dag)

zip_data = BashOperator(
    task_id='load_data',
    bash_command="tar -czvf /opt/airflow/dags/the_log/weblog.tar /opt/airflow/dags/the_log/transformed_data.txt",
    dag=dag)

scanForLog >> extract_logs >> filter_logs >> zip_data
