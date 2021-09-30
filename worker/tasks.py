import os

from celery import Celery
from celery.utils.log import get_task_logger
from dotenv import load_dotenv

load_dotenv('.env')

logger = get_task_logger(__name__)

app = Celery()
app.conf.broker_url = os.environ.get("CELERY_BROKER_URL")
app.conf.result_backend = os.environ.get('CELERY_RESULT_BACKEND')


@app.task()
def event(data: dict):
    logger.info('Got Request - Starting work ')
    print(data)
