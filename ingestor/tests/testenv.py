from dotenv import load_dotenv
import os
import boto3

load_dotenv()

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_DEFAULT_REGION"),
)

print("AWS_ACCESS_KEY_ID:", os.getenv("AWS_ACCESS_KEY_ID"))
print("AWS_DEFAULT_REGION:", os.getenv("AWS_DEFAULT_REGION"))

buckets = s3.list_buckets()
print("Buckets:", [b['Name'] for b in buckets['Buckets']])