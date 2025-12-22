from elasticsearch import Elasticsearch
from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.getenv('db_user')
DB_PASSWORD = os.getenv('db_password')
DB_HOST = os.getenv('db_host')

es = Elasticsearch(
    DB_HOST,
    http_auth=(DB_USER, DB_PASSWORD)
)

def check_db_connection():
    try:
        if es.ping():
            print("Connected to Elasticsearch")
            return True
        else:
            print("Could not connect to Elasticsearch")
            return False
    except Exception as e:
        print(f"Connection failed: {e}")
        return False

def create_index(index_name):
    if not es.indices.exists(index=index_name):
        es.indices.create(index=index_name)
        print(f"Index '{index_name}' created.")
    else:
        print(f"Index '{index_name}' already exists.")