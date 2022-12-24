from datetime import datetime, timedelta
import logging

from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.contrib.sensors.file_sensor import FileSensor

log = logging.getLogger(__name__)

default_args = {
    'dag_id': 'dag_iris',
    'schedule_interval': '@daily',
    'start_date': datetime(2022, 12, 15),
    'catchup': False,
    'tags': ['Assignent']
}

dag = DAG('iris_dag',
          default_args=default_args,
          catchup=False)

sep_train_test = BashOperator(
    task_id='sep_train_test',
    bash_command="python3 /opt/airflow/dags/iris/sep_train_test.py",
    dag=dag)

train_model = BashOperator(
    task_id='train_model',
    bash_command="python3 /opt/airflow/dags/iris/train_model.py",
    dag=dag)

predict = BashOperator(
    task_id='predict',
    bash_command="python3 /opt/airflow/dags/iris/predict.py",
    dag=dag)

sep_train_test >> train_model >> predict