from typing import Optional

from app.models import RemoveBGEntity


class RemoveBGRepository:
    """RemoveBGRepository class to store the processed image data."""

    def create(self, entity: RemoveBGEntity) -> Optional[RemoveBGEntity]:
        """Create row in DynamoDB.

        :param entity: RemoveBGEntity instance.
        :return: None
        """
        try:
            entity.save()
            return entity

        except RemoveBGEntity.DoesNotExist:
            return None

    def get(self, id: str) -> RemoveBGEntity:
        """Get row from DynamoDB.

        :param id: Request ID.
        :return: RemoveBGEntity instance.
        """
        try:
            return RemoveBGEntity.get(id)

        except RemoveBGEntity.DoesNotExist:
            return None

    def update(self, entity: RemoveBGEntity) -> Optional[RemoveBGEntity]:
        """Update row in DynamoDB.

        :param entity: RemoveBGEntity instance.
        :return: None
        """
        try:
            entity.update(
                actions=[
                    RemoveBGEntity.status.set(entity.status),
                    RemoveBGEntity.s3_key_processed.set(entity.s3_key_processed),
                ]
            )
            return entity

        except RemoveBGEntity.DoesNotExist:
            return None

    def delete(self, _id: str) -> None:
        """Delete row from DynamoDB.

        :param _id: Request ID.
        :return: None
        """
        try:
            entity = RemoveBGEntity.get(_id)
            entity.delete()

        except RemoveBGEntity.DoesNotExist:
            return None
