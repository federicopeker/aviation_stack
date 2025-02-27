import logging
import subprocess
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


# Define default arguments
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 2, 26),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

# Define DAG
dag = DAG(
    "etl_flight_data",
    default_args=default_args,
    description="ETL DAG to fetch and store flight data",
    schedule_interval=timedelta(hours=1),  # Runs every hour
    catchup=False,
)


# Define ETL function
def run_etl():
    """Execute the ETL script inside the Airflow container."""
    result = subprocess.run(
        ["python", "/opt/airflow/scripts/etl.py"], capture_output=True, text=True
    )
    print(result.stdout)
    print(result.stderr)


# Define PythonOperator
etl_task = PythonOperator(
    task_id="run_etl",
    python_callable=run_etl,
    dag=dag,
)

etl_task
