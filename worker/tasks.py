import datetime
from dataclasses import dataclass

from celery import Celery
from celery.utils.log import get_task_logger
from sqlalchemy.orm import Session

import crud
import schemas
from db import engine, Base, SessionLocal
from settings import settings

logger = get_task_logger(__name__)
Base.metadata.create_all(engine)


app = Celery()
app.conf.broker_url = settings.broker_url
app.conf.result_backend = settings.result_backend


@dataclass
class EventService:
    db: Session

    def _parse_data(self, data) -> [schemas.SessionCreate, schemas.EventSchema]:
        return (
            schemas.SessionCreate(uuid=data['session_id']),
            schemas.EventSchema(
                category=data['category'],
                name=data['name'],
                data=data['data'],
                timestamp=datetime.datetime.fromisoformat(data['timestamp']),
            ),
        )

    def create(self, data):
        session, event = self._parse_data(data)
        session = crud.session.create(self.db, session)
        crud.event.create(
            self.db, schemas.EventCreate(session_id=session.id, **event.dict())
        )


@app.task()
def event(data: dict):
    logger.info('Got Request - Starting work ')
    EventService(SessionLocal()).create(data)
