from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import pandas as pd
from sqlalchemy import create_engine
# from unidecode import unidecode

# from plugins.mysql_operator import MySQLOperators
from mysql_operator import MySQLOperators
# from plugins.postgresql_operator import PostgresOperators
from postgresql_operator import PostgresOperators

def extract_and_load_to_staging(**kwargs):
    source_operator = MySQLOperators('mysql')
    staging_operator = PostgresOperators('postgres')
    
    tables = [
        "product_category_name_translation",
        "geolocation",
        "sellers",
        "customers",
        "products",
        "orders",
        "order_items",
        "order_payments",
        "order_reviews"
    ]
    
    for table in tables:
        # Trích xuất dữ liệu từ nguồn MySQL
        df = source_operator.get_data_to_pd(f"SELECT * FROM {table}")
        
        # Lưu dữ liệu thô vào schema public trong PostgreSQL
        staging_operator.save_data_to_postgres(
            df,
            f"stg_{table}",
            schema='staging',
            if_exists='replace'
        )
        
        print(f"Đã trích xuất và lưu bảng {table} từ MySQL vào PostgreSQL staging")


# test connect
def test_connect_mysql(**kwargs):
    source_operator = MySQLOperators('mysql')
    staging_operator = PostgresOperators('postgres')
    
    table = "product_category_name_translation"
    
    df = source_operator.get_data_to_pd(f"SELECT * FROM {table}")

    print(df.head())

def test_connect_postgre():
    staging_operator = PostgresOperators('postgres')
    table = "test_2"
    
    df = staging_operator.get_data_to_pd(f"SELECT * FROM staging.{table}")

    print(df.head())