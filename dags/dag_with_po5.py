from airflow import DAG

from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'Archana',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}


def greet(age, ti):
    first_name = ti.xcom_pull(task_ids='get_name', key='first_name')
    last_name = ti.xcom_pull(task_ids='get_name', key='last_name')
    print(f"Hello World! My name is {first_name} {last_name}, and I am {age} years old!")


def get_name(ti):
    ti.xcom_push(key='first_name', value='Avani')
    ti.xcom_push(key='last_name', value='Karpe')
    


with DAG(
    default_args=default_args,
    dag_id='our_first_dag_with_python_operator_v5',
    description='our first dag using python operator',
    start_date=datetime(2023, 2, 1),
    schedule_interval='@daily',
) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet,
        op_kwargs={'age' : '30'}
   )

    task2 = PythonOperator(
        task_id='get_name',
        python_callable=get_name
    )

    task2 >> task1