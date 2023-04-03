"""RemoveBGEntity class to store the processed image data."""


from pynamodb.attributes import UnicodeAttribute
from pynamodb.models import Model

from app.core.config import AWS_DEFAULT_REGION, AWS_DYNAMODB_REMOVEBG_TABLE_NAME


class RemoveBGEntity(Model):
    """RemoveDBEntity class to store the processed image data."""

    class Meta:
        """Meta class for RemoveBGEntity."""

        table_name = AWS_DYNAMODB_REMOVEBG_TABLE_NAME
        region = AWS_DEFAULT_REGION

    id = UnicodeAttribute(hash_key=True)
    s3_key_original = UnicodeAttribute(null=False)
    s3_key_processed = UnicodeAttribute(null=True)
    status = UnicodeAttribute(null=False)

    def __str__(self) -> str:
        return (
            f"RemoveBGEntity(id={self.id}, "
            f"s3_key_original={self.s3_key_original}, "
            f"s3_key_processed={self.s3_key_processed}, "
            f"status={self.status})"
        )

    def __repr__(self) -> str:
        return self.__str__()
