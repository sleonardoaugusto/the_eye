import os

from celery import Celery
from dotenv import load_dotenv
from fastapi import FastAPI
from starlette import status

import schemas

load_dotenv('.env')

app = FastAPI()

celery_app = Celery()
celery_app.conf.broker_url = os.environ.get("CELERY_BROKER_URL")
celery_app.conf.result_backend = os.environ.get('CELERY_RESULT_BACKEND')


@app.post("/event", status_code=status.HTTP_202_ACCEPTED)
def root(event: schemas.EventCreate):
    r = celery_app.send_task('tasks.event', [event.dict()])
    return r.id


@app.get('/event-status/<task_id>')
def get_status(task_id):
    task = celery_app.AsyncResult(task_id, app=celery_app)
    print("Invoking Method ")
    return f"Status of the Task: {task.state}"
