import enum

from sqlalchemy import Column, Integer, ForeignKey, Enum, JSON, TIMESTAMP, String
from sqlalchemy.orm import relationship

from db import Base


class Event(Base):

    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey('sessions.id'))
    category = Column(String)
    name = Column(String)
    data = Column(JSON)
    timestamp = Column(TIMESTAMP)
    session = relationship("Session", back_populates="event")
