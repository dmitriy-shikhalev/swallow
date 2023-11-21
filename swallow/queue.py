from abc import ABC, abstractmethod

from .domain.models import Message


class AbstractQueue(ABC):
    """
    Abstract class for Queue.
    """
    @abstractmethod
    def pull(self) -> Message | None:
        """
        Abstract method "pull".
        """
        raise NotImplementedError

    @abstractmethod
    def push(self, message: Message) -> None:
        """
        Abstract method "push".
        """
        raise NotImplementedError


class InMemoryQueue(AbstractQueue):
    """
    Local queue.
    """
    storage: list[Message]

    def __init__(self):
        self.storage = []

    def push(self, message: Message):
        self.storage.append(message)

    def pull(self) -> Message | None:
        try:
            return self.storage.pop()
        except IndexError:
            return None
