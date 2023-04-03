from pydantic import BaseModel


class SNSNotification(BaseModel):
    Type: str
    Message: str
    Timestamp: str
