import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from hashlib import sha256
from typing import Any, NewType, Sequence


logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class Object:
    """
    Class that implements Args of operator launch.
    """
    args: Sequence[Any] = field(default_factory=list)
    kwargs: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, dict_: dict):
        """
        Convert python-dict to class Args.
        """
        raise NotImplementedError


class AbstractOperator(ABC):
    """
    Abstract class for operators.
    """
    # pylint: disable=too-few-public-methods

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    @abstractmethod
    def __call__(self, args: Object) -> Object:
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
    operator: type[AbstractOperator]

    @classmethod
    def from_dict(cls, dict_: dict):
        """
        Convert python-dict to class Unit.
        """
        raise NotImplementedError


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

    @classmethod
    def from_dict(cls, dict_: dict):
        """
        Convert python-dict to class Ticket.
        """
        raise NotImplementedError

    def __hash__(self):
        return hash(self.ticket_id) ^ hash(self.num) ^ hash(self.is_last)


@dataclass(frozen=True)
class Message:
    """
    Object-value for "message".
    """
    object: Object
    ticket: Ticket

    @classmethod
    def from_dict(cls, dict_: dict):
        """
        Convert python-dict to class Message.
        """
        return cls(
            object=Object.from_dict(dict_['args']),
            ticket=Ticket.from_dict(dict_['ticket']),
        )
