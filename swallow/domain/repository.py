from abc import ABC, abstractmethod

from .models import Aggregate, AggregateKey, Message


class AbstractRepository(ABC):
    """
    Abstract repository.
    """
    @abstractmethod
    def create(self, key: AggregateKey) -> None:
        """
        Create a new aggregate by key.
        """
        raise NotImplementedError

    @abstractmethod
    def get(self, key: AggregateKey) -> Aggregate:
        """
        Get an aggregate by key.
        """
        raise NotImplementedError

    @abstractmethod
    def delete(self, key: AggregateKey) -> None:
        """
        Delete an aggregate by key.
        """
        raise NotImplementedError

    @abstractmethod
    def add(self, key: AggregateKey, message: Message) -> None:
        """
        Add a new message to aggregate by key.
        """
        raise NotImplementedError
