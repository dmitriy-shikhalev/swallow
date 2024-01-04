from abc import ABC, abstractmethod


class Operator(ABC):
    # pylint: disable=too-few-public-methods
    """
    Abstract operator.
    """
    @abstractmethod
    def execute(self):
        """
        Execute operator.
        """
        raise NotImplementedError


class Aggregator(ABC):
    # pylint: disable=too-few-public-methods
    """
    Abstract aggregator.
    """
    @abstractmethod
    def execute(self):
        """
        Add value to aggregator.
        """
        raise NotImplementedError
