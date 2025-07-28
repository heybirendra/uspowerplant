# --- Run All ---
from sqlalchemy import create_engine

from upload import *
from config import *
from ddl.ddl import *
import boto3

# print(f"AWS Key: {AWS_ACCESS_KEY_ID}")
# print(f"AWS Secret: {'set' if AWS_SECRET_ACCESS_KEY else 'not set'}")
# print(f"AWS Region: {AWS_DEFAULT_REGION}")
#
# print("AWS_ACCESS_KEY_ID:", os.getenv("AWS_ACCESS_KEY_ID"))
# print("AWS_SECRET_ACCESS_KEY:", os.getenv("AWS_SECRET_ACCESS_KEY"))
# print("AWS_DEFAULT_REGION:", os.getenv("AWS_DEFAULT_REGION"))

s3client = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_DEFAULT_REGION"),
)

s3resource = boto3.resource(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_DEFAULT_REGION"),
)

# Correctly create both client and resource from the same session
# s3_client = session.client("s3")
# s3_resource = session.resource("s3")  # Now you can call .Bucket()

buckets = s3client.list_buckets()
print("Buckets:", [b['Name'] for b in buckets['Buckets']])

def init(engine) :
    ensure_tables_exist(engine)
    ensure_bucket_exists(s3resource, S3_BUCKET)
    ensure_default_file_exist(s3client, S3_BUCKET, DEFAULT_FILE_NAME,DEFAULT_FILE_PATH)

if __name__ == "__main__":
    engine = create_engine("postgresql://aiq:aiq@postgres:5432/powergen")
    init(engine)
    # ingest(s3_client, engine)