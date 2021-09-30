from unittest.mock import patch

from starlette import status


@patch('main.Celery.send_task')
def test_should_create_event_task(send_task, client, faker):
    payload = {"session_id": faker.uuid4()}
    r = client.post('/event', json=payload)

    assert r.status_code == status.HTTP_202_ACCEPTED
    send_task.assert_called_with('tasks.event', [payload])
