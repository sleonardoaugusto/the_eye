from datetime import datetime

from pydantic import BaseModel


class EventSchema(BaseModel):
    category: str
    name: str
    data: dict
    timestamp: datetime


class EventCreate(EventSchema):
    session_id: str
