import logging
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, NewType, Sequence


logger = logging.getLogger(__name__)


JobID = NewType('JobID', str)
OperatorName = NewType('OperatorName', str)
RequestID = NewType('RequestID', str)
TicketID = NewType('TicketID', str)


class JobStatus(Enum):
    """
    All available statuses of Job.
    """
    PENDING = 'PENDING'
    PROCESSING = 'PROCESSING'
    DONE = 'DONE'
    ERROR = 'ERROR'


class Condition(Enum):
    """
    Condition of starting of operator by count of enter messages.
    """
    ONE = 'ONE'
    ALL = 'ALL'


@dataclass(frozen=True)
class Object:
    """
    Class that implements Args of operator launch.
    """
    args: Sequence[Any] = field(default_factory=list)
    kwargs: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class Request:
    """
    Class for request.
    """
    id: RequestID  # pylint: disable=invalid-name
    operator_name: OperatorName
    input: Object
    output: Object
    exit_code: int | None = None


@dataclass(frozen=True)
class Unit:
    """
    Object-value for "unit".
    """
    operator_name: OperatorName
    condition: Condition


@dataclass(frozen=True)
class Ticket:
    """
    Object-value for "ticket".
    """
    units: Sequence[
        Unit | Sequence[Unit]
    ]


@dataclass(frozen=True)
class Message:
    """
    Object-value for "message".
    """
    id: JobID  # pylint: disable=invalid-name
    object: Object
    ticket: Ticket

    # Block for splitter-aggregator
    num: int | None
    is_last: bool | None


@dataclass(frozen=True)
class Job:
    """
    Class for Job.
    """
    id: JobID  # pylint: disable=invalid-name
    ticket: Ticket
    inputs: Object
    outputs: Object | None
    status: JobStatus = JobStatus.PENDING
