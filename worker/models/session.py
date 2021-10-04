from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db import Base


class Session(Base):
    __tablename__ = 'sessions'

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String, unique=True)
    event = relationship("Event", back_populates="session")
