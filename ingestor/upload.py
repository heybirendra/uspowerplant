import botocore
from config import aws_config

def ensure_bucket_exists(s3_resource, bucket_name):
    bucket = s3_resource.Bucket(bucket_name)
    if bucket.creation_date:
        print(f"Bucket '{bucket_name}' already exists.")
    else:
        print(f"Creating bucket '{bucket_name}'...")
        s3_resource.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={'LocationConstraint': aws_config['region']},
        )
        print("Bucket created.")

def upload_file_if_not_exists(s3_client, bucket, key, file_path):
    try:
        s3_client.head_object(Bucket=bucket, Key=key)
        print(f"'{key}' already exists in '{bucket}'. Skipping upload.")
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == '404':
            print(f"Uploading '{key}' to bucket '{bucket}'...")
            s3_client.upload_file(file_path, bucket, key)
            print("Upload complete.")
        else:
            raise
