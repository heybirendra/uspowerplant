# --- Run All ---
from sqlalchemy import create_engine

from ingest import ingest
from upload import *
from config import *
from ddl.ddl import *
import boto3

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

def init(engine) :
    ensure_tables_exist(engine)
    ensure_bucket_exists(s3resource, S3_BUCKET)
    ensure_default_file_exist(s3client, S3_BUCKET, DEFAULT_FILE_NAME,DEFAULT_FILE_PATH)

if __name__ == "__main__":
    engine = create_engine(os.getenv("DB_CON_URL"))
    init(engine)
    ingest(s3client, engine)