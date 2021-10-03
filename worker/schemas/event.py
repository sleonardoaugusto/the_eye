import enum
from datetime import datetime

from pydantic import BaseModel


class EventSchema(BaseModel):
    category: enum.Enum
    name: enum.Enum
    data: dict
    timestamp: datetime


class EventCreate(EventSchema):
    session_id: str
