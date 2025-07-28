# --- Run All ---
from upload import *
from ingest import *
from config import *
import boto3

session = boto3.Session(
    aws_access_key_id="AKIA25XJBILLRE77QZBK",
    aws_secret_access_key="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",
    region_name="ap-south-1",
)

# Correctly create both client and resource from the same session
s3_client = session.client("s3")
s3_resource = session.resource("s3")  # Now you can call .Bucket()

if __name__ == "__main__":
    ensure_bucket_exists(s3_resource, S3_CONFIG['bucket'])
    upload_file_if_not_exists(s3_client, S3_CONFIG['bucket'], S3_CONFIG['key'], file_config['filepath'])
    ingest_data(s3_client)