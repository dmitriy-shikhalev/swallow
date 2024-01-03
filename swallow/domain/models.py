from __future__ import annotations

import json
import logging
from dataclasses import asdict, dataclass, field

from .file import AbstractFile


logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class Unit:
    """
    Object-value for "unit".
    """
    name: str
    tags: set[str] = field(default_factory=set)


@dataclass(frozen=True)
class Sequence:
    """
    Object-value for "sequence of units".
    """
    element = tuple[Unit | dict[frozenset, 'Sequence'], ...]


@dataclass(frozen=True)
class Ticket:
    """
    Object-value for "ticket".
    """
    sequence: Sequence


@dataclass(frozen=True)
class Message:
    """
    Object-value for "message".
    """
    job_id: str
    object: str
    ticket: Ticket

    @classmethod
    def from_file(cls, file: AbstractFile) -> Message:
        """
        Convert file content to message.
        """
        return cls(
            **json.loads(
                file.read()
            )
        )

    def to_json(self):
        """
        Represent message as json.
        """
        return json.dumps(asdict(self))


AggregateKey = tuple[str, str, str]


@dataclass(frozen=False)
class Aggregate:
    """
    Data class for aggregate.
    """
    key: AggregateKey
    messages: list[Message]
