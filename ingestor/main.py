# --- Run All ---
from sqlalchemy import create_engine

from upload import *
from ingest import *
from config import *
from ddl.ddl import *
import boto3

session = boto3.Session(
    aws_access_key_id="AKIA25XJBILLRE77QZBK",
    aws_secret_access_key="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",
    region_name="ap-south-1",
)

# Correctly create both client and resource from the same session
s3_client = session.client("s3")
s3_resource = session.resource("s3")  # Now you can call .Bucket()

def init(engine) :
    ensure_tables_exist(engine)
    print("bucketname : ",S3_BUCKET)
    ensure_bucket_exists(s3_resource, S3_BUCKET)
    ensure_default_file_exist(s3_client, S3_BUCKET, DEFAULT_FILE_NAME,
                              DEFAULT_FILE_PATH)

if __name__ == "__main__":
    print("aws region from env:", AWS_DEFAULT_REGION)
    engine = create_engine("postgresql://aiq:aiq@postgres:5432/powergen")
    init(engine)
    ingest(s3_client, engine)