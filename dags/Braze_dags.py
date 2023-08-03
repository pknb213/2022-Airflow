
from datetime import datetime, timedelta
from textwrap import dedent
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'Cheon YoungJo',
    'depends_on_past': True,
    'email': ['pknb213@naver.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=15),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
}
with DAG(
    'Braze Update By External_Id API',
    default_args=default_args,
    description='A simple Echo Test DAG',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 8, 3),
    catchup=False,
    tags=['Braze_API'],
) as dag:
    t1 = BashOperator(
        task_id='echo-1',
        bash_command='echo Nice To Meet You',
        retries=3,
    )

    t2 = BashOperator(
        task_id='echo-2',
        depends_on_past=True,
        bash_command='echo Nice To Meet You Too',
        retries=3,
    )

    t3 = BashOperator(
        task_id='echo-3',
        depends_on_past=True,
        bash_command='echo Nice To Meet You Too Too',
        retries=3,
    )

    t1.doc_md = dedent(
        """\
    #### Task Documentation
    You can document your task using the attributes `doc_md` (markdown),
    `doc` (plain text), `doc_rst`, `doc_json`, `doc_yaml` which gets
    rendered in the UI's Task Instance Details page.
    ![img](http://montcs.bloomu.edu/~bobmon/Semesters/2012-01/491/import%20soul.png)

    """
    )

    dag.doc_md = __doc__  # providing that you have a docstring at the beginning of the DAG
    dag.doc_md = """
    This is a documentation placed anywhere
    """  # otherwise, type it like this

    t1 >> t2 >> t3
