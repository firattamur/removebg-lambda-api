import uuid
from io import BytesIO
from typing import Optional

from fastapi import UploadFile
from PIL import Image

from app.core.config import AWS_S3_BUCKET_NAME
from app.core.utils import AWSClients


class AWSS3:
    """
    AWS S3 client to upload and download images.
    """

    def __init__(self):
        """
        Create S3 client and set bucket name.
        """
        self.bucket_name = AWS_S3_BUCKET_NAME

    def upload_image(self, image: UploadFile) -> Optional[str]:
        """
        Uploads an image to S3 bucket and returns S3 key.

        :param image: Image to upload
        :return: S3 key of image, or None if upload failed
        """

        s3_key = f"original/{str(uuid.uuid4())}.jpg"

        try:
            with BytesIO() as output:
                image.file.seek(0)
                output.write(image.file.read())
                output.seek(0)

                AWSClients.s3.upload_fileobj(output, self.bucket_name, s3_key)

            return s3_key

        except Exception as e:
            print(f"Error uploading image to S3: {e}")
            return None

    def download_image(self, s3_key: str) -> Optional[Image.Image]:
        """
        Downloads an image from S3 bucket and returns it as a PIL Image object.

        :param s3_key: S3 key of image
        :return: Image object, or None if download failed
        """

        try:
            with BytesIO() as output:
                AWSClients.s3.download_fileobj(self.bucket_name, s3_key, output)
                output.seek(0)
                image = Image.open(output)

            return image

        except Exception as e:
            print(f"Error downloading image from S3: {e}")
            return None
