from enum import Enum

import boto3

from .config import (
    AWS_ACCESS_KEY_ID,
    AWS_DEFAULT_REGION,
    AWS_SECRET_ACCESS_KEY,
    AWS_SNS_TOPIC_ARN,
    AWS_SQS_QUEUE_URL,
)


def create_boto3_client(service: str) -> boto3.client:
    """Create boto3 client for AWS service."""

    return boto3.client(
        service,
        region_name=AWS_DEFAULT_REGION,
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )


class AWSClients:
    sqs_queue_url = AWS_SQS_QUEUE_URL
    sns_topic_arn = AWS_SNS_TOPIC_ARN

    sqs = create_boto3_client("sqs")
    sns = create_boto3_client("sns")
    dynamodb = create_boto3_client("dynamodb")
    s3 = create_boto3_client("s3")


class Status(Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"
