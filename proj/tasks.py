from numbers import Number
from typing import Iterable

from proj.celery import app


@app.task
def add(x: Number, y: Number) -> Number:
    return x + y


@app.task
def mul(x: Number, y: Number) -> Number:
    return x * y


@app.task
def xsum(numbers: Iterable[Number]) -> Number:
    return sum(numbers)
