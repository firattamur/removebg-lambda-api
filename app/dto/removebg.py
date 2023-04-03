from typing import Optional

from pydantic import BaseModel


class RemoveBGResponse(BaseModel):
    request_id: str
    s3_key_processed: Optional[str]
    status: str
