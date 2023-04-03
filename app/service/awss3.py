from io import BytesIO
from typing import Optional

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

    def upload_image(self, image: Image, s3_key: str) -> bool:
        """

        Upload image to S3 bucket and return S3 key.
        :param image: Image to upload
        :param s3_key: S3 key of image

        :return: S3 key of image

        """

        with BytesIO() as output:
            try:
                image.save(output, format="JPEG")
                output.seek(0)
                AWSClients.s3.upload_fileobj(output, self.bucket_name, s3_key)

                return True

            except Exception as e:
                print(f"Error uploading image to S3: {e}")
                return False

    def download_image(self, s3_key: str) -> Optional[Image.Image]:
        """
        Download image from S3 bucket.
        :param s3_key: S3 key of image
        :return: Image
        """

        with BytesIO() as output:
            try:
                AWSClients.s3.download_fileobj(self.bucket_name, s3_key, output)
                output.seek(0)
                image = Image.open(output)
                return image

            except Exception as e:
                print(f"Error downloading image from S3: {e}")
                return None
