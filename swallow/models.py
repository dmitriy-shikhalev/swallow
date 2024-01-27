from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from typing import Dict, List, Optional

from .enums import Resistor, Status


@dataclass
class Step:
    id: int = field(init=False)
    ticket_id: int = field(init=False)
    operator: str = field(init=False)
    resistor: Resistor = field(init=False)


@dataclass
class Ticket:
    id: int = field(init=False)
    input: Dict[str] = field(default_factory=dict)
    output: Dict[str] = field(default_factory=dict)
    steps: List[Step] = field(default_factory=list)
    jobs: List[Job] = field(default_factory=list)


@dataclass
class Request:
    id: int = field(init=False)
    job_id: int = field(init=False)
    step_id: int = field(init=False)
    request_id: Optional[str] = field(init=False, default=None)
    status: Status = field(init=False)


@dataclass
class Job:
    id: int = field(init=False)
    ticket_id: int = field(init=False)
    step_id: Optional[int] = field(init=False, default=None)
    status: Status = field(init=False)
