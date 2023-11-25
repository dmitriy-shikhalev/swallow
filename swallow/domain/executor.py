from abc import ABC, abstractmethod

from .models import Object, OperatorName, RequestID


class AbstractExecutor(ABC):
    # pylint: disable=too-few-public-methods
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
