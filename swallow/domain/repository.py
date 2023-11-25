from abc import ABC, abstractmethod

from .models import Job, JobID


class AbstractRepository(ABC):
    """
    Abstract class for repository.
    """

    @abstractmethod
    def create(self, job: Job) -> JobID:
        """
        Create new record.
        """
        raise NotImplementedError

    @abstractmethod
    def get(self, id: JobID) -> Job:  # pylint: disable=invalid-name, redefined-builtin
        """
        Get existed record.
        """
        raise NotImplementedError

    @abstractmethod
    def update(self, id: JobID, job: Job):  # pylint: disable=invalid-name, redefined-builtin
        """
        Update existed record.
        """
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: JobID):  # pylint: disable=invalid-name, redefined-builtin
        """
        Delete existed record.
        """
        raise NotImplementedError
