from abc import ABC, abstractmethod

from .models import Message


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
