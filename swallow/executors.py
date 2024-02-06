from __future__ import annotations

from abc import ABC, abstractmethod
from concurrent.futures import Future, ThreadPoolExecutor
from typing import Any
from uuid import uuid4

from .enums import Status
from .operators import OPERATORS


class OperatorException(Exception):
    """
    Error raised in operator
    """


class AbstractExecutor(ABC):
    requests: dict[str, Future]

    def __init__(self):
        self.requests = dict()

    @abstractmethod
    def start(self, operator: str, *args, **kwargs) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_status(self, request_id: str) -> Status:
        raise NotImplementedError

    @abstractmethod
    def get_result(self, request_id: str) -> Any:
        raise NotImplementedError


class LocalThreadExecutor(AbstractExecutor):
    pool: ThreadPoolExecutor

    def __init__(self):
        super().__init__()
        self.pool = ThreadPoolExecutor(max_workers=1)

    def start(self, operator: str, *args, **kwargs) -> str:
        operator_func = OPERATORS[operator]
        future = self.pool.submit(operator_func, *args, **kwargs)
        request_id = uuid4().hex
        self.requests[request_id] = future
        return request_id

    def get_status(self, request_id: str) -> Status:
        if self.requests[request_id].running():
            return Status.PROCESSING
        if self.requests[request_id].exception():
            return Status.ERROR
        if self.requests[request_id].done():
            return Status.DONE
        return Status.NEW

    def get_result(self, request_id: str) -> Any:
        exception = self.requests[request_id].exception()
        if exception is not None:
            raise OperatorException() from exception
        if self.requests[request_id].done():
            return self.requests[request_id].result()
