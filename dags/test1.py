# #
# # Licensed to the Apache Software Foundation (ASF) under one
# # or more contributor license agreements.  See the NOTICE file
# # distributed with this work for additional information
# # regarding copyright ownership.  The ASF licenses this file
# # to you under the Apache License, Version 2.0 (the
# # "License"); you may not use this file except in compliance
# # with the License.  You may obtain a copy of the License at
# #
# #   http://www.apache.org/licenses/LICENSE-2.0
# #
# # Unless required by applicable law or agreed to in writing,
# # software distributed under the License is distributed on an
# # "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# # KIND, either express or implied.  See the License for the
# # specific language governing permissions and limitations
# # under the License.

# """
# Example DAG demonstrating the usage of the TaskFlow API to execute Python functions natively and within a
# virtual environment.
# """
# import logging
# import shutil
# import time
# from pprint import pprint

# import pendulum

# from airflow import DAG
# from airflow.decorators import task

# from airflow.contrib.sensors.file_sensor import FileSensor


# log = logging.getLogger(__name__)



# with DAG(
#     dag_id='process_web_log',
#     schedule_interval='@daily',
#     start_date=pendulum.datetime(2022, 12, 15),
#     catchup=False,
#     tags=['Assignemt'],
# ) as dag:

#     @task(task_id="dummy_task_1")
#     def dummy_task_1(ds=None, **kwargs):
#         log.warning("inside dummy task!")
#     dummy_task = dummy_task_1()
    
#     # task #1, scan a folder for a log 
#     @task.sensor(task_id="scan_for_log", poke_interval=300, timeout=3600, mode="poke", file_path ='./the_folder/')
#     def scan_a_folder(ds=None, **kwargs):
#         log.warning("scanning a folder ")
#         scan_for_log_task = FileSensor( task_id= "scan_for_log", poke_interval=300)
#         log.warning("scanning a folder finished")
#     scan_folder = scan_a_folder()
    
#     dummy_task >> scan_folder 

#     # # [START howto_operator_python_kwargs]
#     # # Generate 5 sleeping tasks, sleeping from 0.0 to 0.4 seconds respectively
#     # for i in range(5):

#     #     @task(task_id=f'sleep_for_{i}')
#     #     def my_sleeping_function(random_base):
#     #         """This is a function that will run within the DAG execution"""
#     #         time.sleep(random_base)

#     #     sleeping_task = my_sleeping_function(random_base=float(i) / 10)

#     #     run_this >> sleeping_task
#     # # [END howto_operator_python_kwargs]

#     # if not shutil.which("virtualenv"):
#     #     log.warning("The virtalenv_python example task requires virtualenv, please install it.")
#     # else:
#     #     # [START howto_operator_python_venv]
#     #     @task.virtualenv(
#     #         task_id="virtualenv_python", requirements=["colorama==0.4.0"], system_site_packages=False
#     #     )
#     #     def callable_virtualenv():
#     #         """
#     #         Example function that will be performed in a virtual environment.

#     #         Importing at the module level ensures that it will not attempt to import the
#     #         library before it is installed.
#     #         """
#     #         from time import sleep

#     #         from colorama import Back, Fore, Style

#     #         print(Fore.RED + 'some red text')
#     #         print(Back.GREEN + 'and with a green background')
#     #         print(Style.DIM + 'and in dim text')
#     #         print(Style.RESET_ALL)
#     #         for _ in range(10):
#     #             print(Style.DIM + 'Please wait...', flush=True)
#     #             sleep(10)
#     #         print('Finished')

#     #     virtualenv_task = callable_virtualenv()
#     #     # [END howto_operator_python_venv]