# celery-tutorial

This project runs into "Remote - Containers" Visual Studio Code extension.

## Running

1) Start the RabbitMQ Server in backgroud
```shell
$ sudo rabbitmq-server -detached
```

2) Running the Celery worker server
```bash
$ cd src/
$ celery -A tasks worker --loglevel=INFO
```

3) Calling the task
```python
>>> from tasks import add
>>> add.delay(4, 4)
```
