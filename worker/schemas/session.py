from pydantic import BaseModel


class SessionSchema(BaseModel):
    uuid: str


class SessionCreate(SessionSchema):
    ...
