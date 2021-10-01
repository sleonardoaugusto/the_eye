import tasks

from db import SessionLocal
from models import Session


def test_should_create_event(faker):
    payload = {'session_id': faker.uuid4()}
    tasks.event(payload)
    db = SessionLocal()
    assert db.query(Session).filter(Session.id == payload['session_id'])
