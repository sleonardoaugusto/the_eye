import datetime

import tasks
from models import Event


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
