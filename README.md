# celery-tutorial

This project runs into "Remote - Containers" Visual Studio Code extension.

## Running

1) Start the RabbitMQ Server in backgroud
```shell
$ sudo rabbitmq-server -detached
```

2) Running the Celery worker server
```bash
$ celery -A proj worker -l INFO
```

3) Calling the task
```python
>>> from proj.tasks import add

>>> add.delay(2, 2)
```
