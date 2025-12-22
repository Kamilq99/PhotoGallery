from s3_connect.s3connect import check_connection, list_buckets
from db_connect.elastic_connect import check_db_connection, create_index

def s3_check_connection():
    s3check = check_connection()

def list_s3_buckets():
    buckets = list_buckets()

def init_elastic_config(app):
    dbcheck = check_db_connection()

def init_elastic_index(app, index_name):
    create_index(index_name)