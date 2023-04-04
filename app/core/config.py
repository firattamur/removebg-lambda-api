import os

import dotenv

# Load environment variables from .env file in root directory
dotenv.load_dotenv()

# AWS Credetials
AWS_ACCESS_KEY_ID = os.environ.get("APP_AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("APP_AWS_SECRET_ACCESS_KEY")
AWS_DEFAULT_REGION = os.environ.get("APP_AWS_DEFAULT_REGION")

# AWS S3
AWS_S3_BUCKET_NAME = os.environ.get("APP_AWS_S3_BUCKET_NAME", "fastapi-removebg-bucket")

# AWS SQS
AWS_SQS_QUEUE_URL = os.environ.get("APP_AWS_SQS_QUEUE_URL")
AWS_SNS_TOPIC_ARN = os.environ.get("APP_AWS_SNS_TOPIC_ARN")

# AWS DynamoDB
AWS_DYNAMODB_REMOVEBG_TABLE_NAME = os.environ.get(
    "APP_AWS_DYNAMODB_REMOVEBG_TABLE_NAME"
)

# Default values
STAGE = os.environ.get("STAGE", "")
