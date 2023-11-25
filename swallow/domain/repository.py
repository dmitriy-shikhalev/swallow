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
    def get(self, pk: JobID) -> Job:  # pylint: disable=invalid-name
        """
        Get existed record.
        """
        raise NotImplementedError

    @abstractmethod
    def update(self, pk: JobID, job: Job):  # pylint: disable=invalid-name
        """
        Update existed record.
        """
        raise NotImplementedError

    @abstractmethod
    def delete(self, pk: JobID):  # pylint: disable=invalid-name
        """
        Delete existed record.
        """
        raise NotImplementedError
