from abc import ABC, abstractmethod

from swallow.domain.models import Object, OperatorName, RequestID


class AbstractExecutor(ABC):
    """
    Abstract class for operators.
    """

    @abstractmethod
    def __init__(self):
        raise NotImplementedError

    @abstractmethod
    def execute(self, operator_name: OperatorName, input: Object) -> RequestID:  # pylint: disable=redefined-builtin
        """
        Execute an operator by operator_name and object
        """
        raise NotImplementedError  # pragma: no cover
