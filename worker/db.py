import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv('.env')


engine = create_engine(os.environ.get('SQLALCHEMY_DATABASE_URL'), echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, index=True)
