from abc import ABC, abstractmethod
from typing import Sequence


class AbstractFile(ABC):
    """
    Abstract class for files.
    """
    filename: str

    def __init__(self, filename: str) -> None:
        self.filename = filename

    @abstractmethod
    def read(self) -> bytes:
        """
        Read data from file.
        """
        raise NotImplementedError

    @abstractmethod
    def write(self, bs: bytes) -> None:  # pylint: disable=invalid-name
        """
        Write data to files.
        """
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def listdir(cls) -> Sequence[str]:
        """
        Get list of files.
        """
        raise NotImplementedError

    @abstractmethod
    def delete(self):
        """
        Delete a file.
        """
        raise NotImplementedError
