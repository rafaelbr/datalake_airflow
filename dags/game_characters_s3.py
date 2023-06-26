import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.amazon.aws.transfers.local_to_s3 import LocalFilesystemToS3Operator
from airflow.providers.postgres.hooks.postgres import PostgresHook


def save_data_into_csv():
    pg_hook = PostgresHook(postgres_conn_id='PG_GAMEDB')
    conn = pg_hook.get_conn()
    pg_hook.copy_expert(
        sql="""
            COPY (SELECT * FROM public.characters) TO STDOUT WITH HEADER CSV
        """,
        filename='/tmp/characters.csv'
    )
    conn.commit()

with DAG(
    dag_id='game_characters_s3',
    start_date=datetime.datetime(2023, 6, 23),
    schedule_interval='@daily',
    catchup=False
) as dag:
    save_data = PythonOperator(
        task_id='save_data',
        python_callable=save_data_into_csv
    )

    upload_to_s3 = LocalFilesystemToS3Operator(
        task_id='upload_to_s3',
        aws_conn_id='AWS_SANDBOX',
        filename='/tmp/characters.csv',
        dest_key='gamedb/characters/csv/characters_{}.csv'.format(datetime.datetime.now().strftime('%Y%m%d')),
        dest_bucket='geekfoxlab-sb-raw'
    )

    save_data >> upload_to_s3

