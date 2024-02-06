import json
from dataclasses import dataclass
from io import IOBase
from typing import Any


@dataclass(frozen=True)
class Int:
    value: int

    def write(self, stream: IOBase) -> None:
        stream.write(
            json.dumps(self.value)
        )

    @classmethod
    def decode(cls, stream: IOBase) -> 'Int':
        data = stream.read()
        return cls(json.loads(data.decode("utf")))


@dataclass(frozen=True)
class Float:
    value: float

    def encode(self):
        return json.dumps(self.value)

    @classmethod
    def decode(cls, value):
        return cls(json.loads(value))


@dataclass(frozen=True)
class Str:
    value: str

    def encode(self):
        return json.dumps(self.value)

    @classmethod
    def decode(cls, value):
        return cls(json.loads(value))


@dataclass(frozen=True)
class Dict:
    value: dict[Any, Any]

    def encode(self):
        return json.dumps(self.value)

    @classmethod
    def decode(cls, value):
        return cls(json.loads(value))


@dataclass(frozen=True)
class List:
    value: list[Any]

    def encode(self):
        return json.dumps(self.value)

    @classmethod
    def decode(cls, value):
        return cls(json.loads(value))
