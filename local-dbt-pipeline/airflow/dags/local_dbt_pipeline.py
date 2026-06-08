from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator


DBT_PROJECT_DIR = "/opt/airflow/dbt_project"


with DAG(
    dag_id="local_dbt_pipeline",
    description="Airflow DAG that runs dbt seed, dbt run, and dbt test",
    start_date=datetime(2026, 4, 30),
    schedule=None,
    catchup=False,
    tags=["week4", "dbt", "airflow", "local-pipeline"],
) as dag:

    clean_dbt_cache = BashOperator(
        task_id="clean_dbt_cache",
        bash_command=f"cd {DBT_PROJECT_DIR} && rm -rf target dbt_packages logs",
    )

    dbt_seed = BashOperator(
        task_id="dbt_seed",
        bash_command=f"cd {DBT_PROJECT_DIR} && dbt seed",
    )

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command=f"cd {DBT_PROJECT_DIR} && dbt run",
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command=f"cd {DBT_PROJECT_DIR} && dbt test",
    )

    clean_dbt_cache >> dbt_seed >> dbt_run >> dbt_test