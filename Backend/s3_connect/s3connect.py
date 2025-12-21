import boto3
import os
from dotenv import load_dotenv

load_dotenv()

AWS_S3_URL = os.getenv('AWS_URL_S3')
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_DEFAULT_REGION = os.getenv('AWS_DEFAULT_REGION')

s3 = boto3.client(
    's3',
    endpoint_url=AWS_S3_URL,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_DEFAULT_REGION
)

def check_connection():
    try:
        s3.list_buckets()
        return True
    except Exception as e:
        print(f"Connection failed: {e}")
        return False

def list_buckets():
    try:
        response = s3.list_buckets()
        return [bucket['Name'] for bucket in response.get('Buckets', [])]
    except Exception as e:
        print(f"Error listing buckets: {e}")
        return []