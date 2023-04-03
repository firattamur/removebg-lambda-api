from fastapi import APIRouter, Depends, File, UploadFile, status

from app.core.logging import logger
from app.dto import RemoveBGResponse, SNSNotification
from app.service import RemoveBGService

router = APIRouter()


@router.post(
    "/removebg",
    tags=["removebg"],
    response_model=RemoveBGResponse,
    status_code=status.HTTP_201_CREATED,
)
async def removebg(image: UploadFile = File(...), service: RemoveBGService = Depends()):
    """
    Upload an image and remove the background.

    :param image    : Image to remove background from.
    :param service  : RemoveBGService instance.
    :return         : Image with background removed.
    """
    logger.info(f"remove background from image request received: {image.filename}")

    return service.remove_background(image)


@router.post(
    "/sns-notification",
    tags=["removebg"],
    status_code=status.HTTP_201_CREATED,
    include_in_schema=False,
)
async def sns_notification(
    notification: SNSNotification, service: RemoveBGService = Depends()
):
    """
    Process SNS notification.

    :param sns_notification: SNS notification.
    :return: None
    """
    logger.info(f"sns notification received: {sns_notification}")

    return service.process_sns_notification(sns_notification)
