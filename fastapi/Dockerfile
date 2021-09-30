FROM python:3.8-slim

COPY requirements.txt /
RUN pip install -r /requirements.txt

ADD . /fastapi
WORKDIR /fastapi

CMD uvicorn main:app --reload --host 0.0.0.0 --port 8000
