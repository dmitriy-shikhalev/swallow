from abc import ABC, abstractmethod

from .models import AggregateKey, Message


class AbstractRepository(ABC):
    """
    Abstract repository.
    """
    @abstractmethod
    def create(self, key: AggregateKey):
        """
        Create a new aggregate by key.
        """
        raise NotImplementedError

    @abstractmethod
    def get(self, key: AggregateKey):
        """
        Get an aggregate by key.
        """
        raise NotImplementedError

    @abstractmethod
    def delete(self, key: AggregateKey):
        """
        Delete an aggregate by key.
        """
        raise NotImplementedError

    @abstractmethod
    def add(self, key: AggregateKey, message: Message):
        """
        Add a new message to aggregate by key.
        """
        raise NotImplementedError
