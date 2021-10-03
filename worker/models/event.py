import enum

from sqlalchemy import Column, Integer, ForeignKey, Enum, JSON, TIMESTAMP
from sqlalchemy.orm import relationship

from db import Base


class Event(Base):
    class Category(enum.Enum):
        PAGE_INTERACTION = 'page interaction'
        FORM_INTERACTION = 'form interaction'

    class Name(enum.Enum):
        PAGE_VIEW = 'pageview'
        CTA_CLICK = 'cta click'
        SUBMIT = 'submit'

    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey('sessions.id'))
    category = Column(Enum(Category))
    name = Column(Enum(Name))
    data = Column(JSON)
    timestamp = Column(TIMESTAMP)
    session = relationship("Session", back_populates="event")
