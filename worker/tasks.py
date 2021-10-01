from dataclasses import dataclass

from celery import Celery
from celery.utils.log import get_task_logger
from sqlalchemy.orm import session

from db import engine, Base, SessionLocal
from models import Session
from settings import settings

logger = get_task_logger(__name__)
Base.metadata.create_all(engine)


app = Celery()
app.conf.broker_url = settings.broker_url
app.conf.result_backend = settings.result_backend


@dataclass
class EventService:
    db: session.Session

    def _extract_data(self, data):
        return {'id': data['session_id']}

    def create(self, data):
        data_extracted = self._extract_data(data)
        db_obj = Session(**data_extracted)
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)


@app.task()
def event(data: dict):
    logger.info('Got Request - Starting work ')
    EventService(SessionLocal()).create(data)
