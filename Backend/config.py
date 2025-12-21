from s3_connect.s3connect import check_connection, list_buckets
from db_connect.dbconnect import check_db_connection, create_index

def init_s3_config(app):
    s3check = check_connection()

def init_s3_buckets(app):
    buckets = list_buckets()
    app.config['S3_BUCKETS'] = buckets

def init_elastic_config(app):
    from db_connect.dbconnect import check_db_connection
    dbcheck = check_db_connection()

def init_elastic_index(app, index_name):
    from db_connect.dbconnect import create_index
    create_index(index_name)