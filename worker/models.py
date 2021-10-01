from sqlalchemy import Column, Integer, String, ForeignKey

from db import Base


class Session(Base):
    __tablename__ = 'sessions'

    id = Column(String, primary_key=True, index=True)


class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String, ForeignKey('sessions.id'))
