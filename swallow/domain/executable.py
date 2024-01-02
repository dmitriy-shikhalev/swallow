from abc import ABC, abstractmethod


class Operator(ABC):
    # pylint: disable=too-few-public-methods
    """
    Abstract operator.
    """
    raise NotImplementedError


class Aggregator(ABC):
    # pylint: disable=too-few-public-methods
    """
    Abstract aggregator.
    """
    raise NotImplementedError
