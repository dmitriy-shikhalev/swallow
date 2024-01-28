from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from typing import Dict, List, Optional

from .enums import Resistor, Status


@dataclass
class Input:
    id: int = field(init=False)
    name: str = field(init=False)
    type: str = field(init=False)
    resistor: Resistor = field(init=False)


@dataclass
class Output:
    id: int = field(init=False)
    name: str = field(init=False)
    type: str = field(init=False)


@dataclass
class Operator:
    """
    Abstract operator.
    """
    id: int = field(init=False)
    name: str = field(init=False)
    input: list[Input] = field(default_factory=dict)
    output: list[Output] = field(default_factory=dict)


@dataclass
class Unit:
    id: int = field(init=False)
    ticket_id: int = field(init=False)
    name: str = field(init=False)
    operator: Operator = field(init=False)


@dataclass
class Ticket:
    id: int = field(init=False)
    input: Dict[str, str] = field(default_factory=dict)
    output: Dict[str, str] = field(default_factory=dict)
    units: List[Unit] = field(default_factory=list)
    jobs: List[Job] = field(default_factory=list)


@dataclass
class Request:
    id: int = field(init=False)
    job_id: int = field(init=False)
    unit_id: int = field(init=False)
    request_id: Optional[str] = field(init=False, default=None)
    grid: str = field(init=False)  # Для контроля по каким инпутам (файлам) запущен данный юнит.
    status: Status = field(init=False)


@dataclass
class Job:
    id: int = field(init=False)
    ticket_id: int = field(init=False)
    unit_id: Optional[int] = field(init=False, default=None)
    status: Status = field(init=False)
