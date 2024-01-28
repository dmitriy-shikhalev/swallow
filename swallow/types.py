import json
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Int:
    value: int

    def encode(self):
        return json.dumps(self.value)

    @classmethod
    def decode(cls, value):
        return cls(json.loads(value))


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
class Json:
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
