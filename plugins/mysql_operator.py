from airflow.providers.mysql.hooks.mysql import MySqlHook
import logging
from contextlib import closing
import os

class MySQLOperators:
    def __init__(self, conn_id='mysql'):
        try:
            self.mysqlhook = MySqlHook(mysql_conn_id=conn_id)
            self.mysql_conn = self.mysqlhook.get_conn()
        except Exception as e:
            logging.error(f"Can't connect to {conn_id} database. Error: {e}")

    def get_data_to_pd(self, query=None):
        return self.mysqlhook.get_pandas_df(query)
   
    def get_records(self, query):
        return self.mysqlhook.get_records(query)
    
    def execute_query(self, query):
        try:
            cur = self.mysql_conn.cursor()
            cur.execute(query)
            self.mysql_conn.commit()
        except:
            logging.ERROR(f"cant execute query: {query}")