import os

import dotenv

# Load environment variables from .env file in root directory
dotenv.load_dotenv()

# AWS Credetials
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_DEFAULT_REGION = os.environ.get("AWS_DEFAULT_REGION")

# AWS S3
AWS_S3_BUCKET_NAME = os.environ.get("AWS_S3_BUCKET_NAME", "image-resizer-bucket")

# AWS SQS
AWS_SQS_QUEUE_URL = os.environ.get("AWS_SQS_QUEUE_NAME")
AWS_SNS_TOPIC_ARN = os.environ.get("AWS_SNS_TOPIC_NAME")

# AWS DynamoDB
AWS_DYNAMODB_TABLE_NAME = os.environ.get("AWS_DYNAMODB_TABLE_NAME")

# Default values
STAGE = os.environ.get("STAGE", "")
