from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# Default settings for our tasks
default_args = {
    'owner': 'data_engineer',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG (The blueprint for our pipeline)
with DAG(
    'customer_churn_pyspark_etl',
    default_args=default_args,
    description='Runs the PySpark Churn ETL pipeline to BigQuery daily',
    schedule_interval='@daily', # Run this every day at midnight!
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=['churn', 'pyspark', 'bigquery'],
) as dag:

    # Define the Task using a BashOperator to run our PySpark script
    run_pyspark_job = BashOperator(
        task_id='run_pyspark_etl_script',
        # In a real Airflow server, this path would point to where the script lives on the server
        bash_command='cd /opt/airflow/src && python 02_pyspark_etl.py',
    )
    
    # If we had more steps (like a data quality check), we would chain them here!
    # e.g., run_pyspark_job >> data_quality_check
