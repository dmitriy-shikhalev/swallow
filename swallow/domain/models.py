import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, NewType, Sequence


logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class Object:
    """
    Class that implements Args of operator launch.
    """
    args: Sequence[Any] = field(default_factory=list)
    kwargs: dict[str, Any] = field(default_factory=dict)


class AbstractOperator(ABC):
    """
    Abstract class for operators.
    """
    # pylint: disable=too-few-public-methods

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @abstractmethod
    def __call__(self, object: Object) -> Object:  # pylint: disable=redefined-builtin
        raise NotImplementedError  # pragma: no cover


Channel = NewType('Channel', str)
TicketID = NewType('TicketID', str)


class ChannelEnum(Enum):
    """
    Preset communication channels for enter, exit and error.
    """
    ENTER = Channel('enter')
    EXIT = Channel('exit')
    ERROR = Channel('error')


@dataclass(frozen=True)
class Unit:
    """
    Object-value for "unit".
    """
    channel: Channel
    operator: AbstractOperator


@dataclass(frozen=True)
class Ticket:
    """
    Object-value for "ticket".
    """
    ticket_id: TicketID
    units: Sequence[Unit]

    # Block for splitter-aggregator
    num: int = 0
    is_last: bool = True
    count: int | None = None


@dataclass(frozen=True)
class Message:
    """
    Object-value for "message".
    """
    object: Object
    ticket: Ticket
