# The Eye

## How to use?
1. Create an Event
```
curl -X 'POST' \
  'http://localhost:8000/event' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "session_id": "string",
  "category": "page interaction",
  "name": "pageview",
  "data": {"key": "value"},
  "timestamp": "2021-01-01 09:15:27.243860"
}'
```

2. Monitor the progress
- Accessing flower:
```http://localhost:5555/tasks```

- API REST:
```
curl -X 'GET' \
  'http://localhost:8000/event-status/<task_id>?task_id=[task-id]' \
  -H 'accept: application/json'
``` 

## API documentation
You can visit the API documentation with http://localhost:8000/docs


## How develop?

1. Clone this repo.
2. Fire up docker containers.
3. Run tests

```console
git clone git@github.com:sleonardoaugusto/the_eye.git
cd the_eye
docker-compose up -d --build
docker exec -i -t [container name] 'pytest'
```
