# from dotenv import load_dotenv
# import os
#
# dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '.env'))
# load_dotenv(dotenv_path=dotenv_path)
#
# AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
# AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
# AWS_DEFAULT_REGION = os.getenv("AWS_DEFAULT_REGION", "us-east-1")
#
# S3_BUCKET = os.getenv("S3_BUCKET")
#
# DEFAULT_FILE_NAME = os.getenv("DEFAULT_FILE_NAME")
#
# DEFAULT_FILE_PATH = os.getenv("DEFAULT_FILE_PATH")
#
# # S3_CONFIG = {
# #     'bucket': 'uspowerplantdata',
# #     'key': 'GEN23.csv'
# # }
# #
# # aws_config = {
# #     'region': 'ap-south-1',
# #     'access_key_id': 'AKIA25XJBILLRE77QZBK',
# #     'secret_access_key': '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'
# # }
# #
# # file_config = {
# #     'filepath' : './GEN23.csv'
# # }
#
#

import os
from dotenv import load_dotenv
#
# current_dir = os.path.dirname(os.path.abspath(__file__))
#
# project_root = os.path.abspath(os.path.join(current_dir, '..'))
#
# dotenv_path = os.path.join(project_root, '.env')
# print(f"Loading .env from: {dotenv_path}")

load_dotenv()

# Step 5: Use environment variables

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_DEFAULT_REGION=os.getenv('AWS_DEFAULT_REGION')

S3_BUCKET = os.getenv('S3_BUCKET')
DEFAULT_FILE_NAME=os.getenv('DEFAULT_FILE_NAME')
DEFAULT_FILE_PATH=os.getenv('DEFAULT_FILE_PATH')
POSTGRES_PASSWORD=os.getenv('POSTGRES_PASSWORD')


