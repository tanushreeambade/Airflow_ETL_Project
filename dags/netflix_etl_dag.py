from airflow.sdk import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd

def extract():
    print("Extracting Netflix Data...")

    df = pd.read_csv("/opt/airflow/data/netflix_titles.csv")

    print(df.head())
    print(f"Total Rows: {len(df)}")

    df.to_csv("/opt/airflow/data/netflix_extracted.csv", index=False)

    print("Extraction Completed")

def transform():
    print("Transforming Netflix Data...")

    import pandas as pd

    df = pd.read_csv("/opt/airflow/data/netflix_extracted.csv")

    print("Missing values:")
    print(df.isnull().sum())

    print("Duplicate rows:", df.duplicated().sum())

    df.columns = df.columns.str.lower()

    df.to_csv("/opt/airflow/data/netflix_transformed.csv", index=False)

    print("Transformation Completed")

def load():
    print("Loading Data to PostgreSQL...")

    import pandas as pd
    from sqlalchemy import create_engine

    df = pd.read_csv("/opt/airflow/data/netflix_transformed.csv")

    # Rename cast column to match PostgreSQL table
    df = df.rename(columns={"cast": "cast_members"})

    engine = create_engine(
        "postgresql+psycopg2://airflow:airflow@postgres:5432/airflow"
    )

    df.to_sql(
        "netflix_data",
        engine,
        if_exists="replace",
        index=False,
    )

    print(f"Loaded {len(df)} records into PostgreSQL")

with DAG(
    dag_id="netflix_etl_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:

    extract_task = PythonOperator(
        task_id="extract",
        python_callable=extract,
    )

    transform_task = PythonOperator(
        task_id="transform",
        python_callable=transform,
    )

    load_task = PythonOperator(
        task_id="load",
        python_callable=load,
    )

    extract_task >> transform_task >> load_task