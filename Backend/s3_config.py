import boto3

s3 = boto3.client(
    "s3",
    endpoint_url='http://localhost:4566',
    aws_access_key_id ='YOUR_AWS_ACCESS_KEY_ID',
    aws_secret_access_key ='YOUR_AWS_SECRET_ACCESS_KEY',
    region_name ='us-east-1',
)

BUCKET_NAME = 'your-bucket-name'