import datetime
import enum

from pydantic import BaseModel


class Category(enum.Enum):
    PAGE_INTERACTION = 'page interaction'
    FORM_INTERACTION = 'form interaction'


class Name(enum.Enum):
    PAGE_VIEW = 'pageview'
    CTA_CLICK = 'cta click'
    SUBMIT = 'submit'


class EventCreate(BaseModel):
    session_id: str
    category: Category
    name: Name
    data: dict
    timestamp: datetime.datetime

    class Config:
        use_enum_values = True
