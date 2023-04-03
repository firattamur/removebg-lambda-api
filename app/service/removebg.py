import json
import uuid

from fastapi import Depends, UploadFile

from app.core.logging import logger
from app.core.utils import AWSClients, Status
from app.dto import RemoveBGResponse, SNSNotification
from app.models import RemoveBGEntity
from app.repository import RemoveBGRepository

from .awss3 import AWSS3


class RemoveBGService:
    """Remove background from image service.

    1. Uploads image to AWS S3 and sends the S3 key to an SQS queue for EC2 workers to process.
    2. Stores a row in DynamoDB with the S3 key, request ID, and status.
    3. Subscribes to an SNS topic to receive notifications when the worker is done processing the image.
    """

    def __init__(
        self,
        awss3: AWSS3 = Depends(),
        repository: RemoveBGRepository = Depends(),
    ):
        """Initialize service.

        :param awss3: AWSS3 instance.

        :return: None
        """
        self.awss3 = awss3
        self.repository = repository

    def remove_background(self, image: UploadFile) -> RemoveBGResponse:
        """Remove background from image.

        :param image: Image to remove background from.
        :return: Image with background removed.
        """
        logger.info(f"remove background from image request received: {image.filename}")

        s3_key_original = self.awss3.upload_image(image)
        entity = self.create_dynamodb_row(s3_key_original)
        self.send_message_to_sqs(s3_key_original, entity.id)

        return RemoveBGResponse(
            request_id=entity.id, s3_key_processed=None, status=entity.status
        )

    def send_message_to_sqs(self, s3_key: str, request_id: str) -> dict:
        """Send message to SQS queue.

        :param s3_key: S3 key of image.
        :return: None
        """
        message = {"s3_key_original": s3_key, "request_id": request_id}
        message_json = json.dumps(message)
        response = AWSClients.sqs.send_message(
            QueueUrl=AWSClients.sqs_queue_url, MessageBody=message_json
        )

        return response

    def process_sns_notification(self, sns_notification: SNSNotification):
        """Process SNS notification.

        :param sns_notification: SNS notification.
        :return: None
        """
        message = json.loads(sns_notification.message)
        request_id = message["request_id"]
        s3_key = message["s3_key_processed"]

        self.update_dynamodb_row(request_id, s3_key)

    def create_dynamodb_row(self, s3_key_original: str) -> str:
        """Create row in DynamoDB.

        :param s3_key_original: S3 key of image.
        :return: Request ID.
        """

        entity = RemoveBGEntity(
            id=uuid.uuid4(),
            s3_key_original=s3_key_original,
            s3_key_processed=None,
            status=Status.PROCESSING.value,
        )

        self.repository.create(entity)

        return entity

    def update_dynamodb_row(self, request_id: str, s3_key_processed: str):
        """Update row in DynamoDB.

        :param request_id: Request ID.
        :param s3_key_processed: S3 key of processed image.
        :return: None
        """
        entity = self.repository.get(request_id)
        entity.s3_key_processed = s3_key_processed
        entity.status = Status.COMPLETED.value

        self.repository.update(entity)
