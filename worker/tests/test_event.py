import datetime

import pytest

import crud
import models
import schemas
import tasks
from models import Event, Session

print(crud, schemas, Session)


def test_should_create_event(faker, db):
    payload = {
        'session_id': faker.uuid4(),
        'category': 'page interaction',
        'name': 'pageview',
        'data': {'key': 'value'},
        'timestamp': datetime.datetime.fromisoformat('2021-01-01 09:15:27.243860'),
    }
    tasks.event(payload)
    event = db.query(Event).first()
    assert event.session.uuid == payload['session_id']
    assert event.category == payload['category']
    assert event.name == payload['name']
    assert event.data == payload['data']
    assert event.timestamp == payload['timestamp']


@pytest.fixture
def fix_session(faker, db):
    obj_in = schemas.SessionCreate(uuid=faker.uuid4())
    obj_in_data = obj_in.dict()
    db_obj = models.Session(**obj_in_data)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def test_should_associate_event_to_session(fix_session, faker, db):
    instance = crud.session.create(db, schemas.SessionCreate(uuid=faker.uuid4()))
    payload = {
        'session_id': instance.uuid,
        'category': 'page interaction',
        'name': 'pageview',
        'data': {'key': 'value'},
        'timestamp': datetime.datetime.fromisoformat('2021-01-01 09:15:27.243860'),
    }
    tasks.event(payload)
    assert db.query(Session).filter_by(uuid=instance.uuid).count() == 1
    assert db.query(Event).count() == 1
