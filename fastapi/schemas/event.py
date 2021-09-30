from pydantic import BaseModel


class EventCreate(BaseModel):
    session_id: str
