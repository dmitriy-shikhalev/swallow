import sqlite3
from abc import ABC, abstractmethod
from typing import Any

from .domain.models import Job


class AbstractRepository(ABC):
    """
    Abstract class for repository.
    """

    @abstractmethod
    def create(self, job: Job) -> Any:
        """
        Create new record.
        """
        raise NotImplementedError

    @abstractmethod
    def get(self, pk: Any) -> Job:  # pylint: disable=invalid-name
        """
        Get existed record.
        """
        raise NotImplementedError

    @abstractmethod
    def update(self, pk: Any, job: Job):  # pylint: disable=invalid-name
        """
        Update existed record.
        """
        raise NotImplementedError


class SqliteRepository(AbstractRepository):
    """
    Class SQLite repository.
    """
    def __init__(self, name: str):
        self.name = name
        self.db = sqlite3.connect(name)  # pylint: disable=invalid-name
