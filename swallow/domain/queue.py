from abc import ABC, abstractmethod

from .models import Message


class AbstractQueue(ABC):
    """
    Abstract class for Queue.
    """
    @abstractmethod
    def pop(self) -> Message | None:
        """
        Abstract method "pop".
        """
        raise NotImplementedError

    @abstractmethod
    def append(self, message: Message) -> None:
        """
        Abstract method "append".
        """
        raise NotImplementedError
