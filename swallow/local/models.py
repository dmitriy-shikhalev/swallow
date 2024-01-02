from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

from ..domain.models import AbstractFile


@dataclass(frozen=True)
class LocalFile(AbstractFile):
    """
    Class for local file.
    """
    path: Path

    def read(self):
        with open(self.path, 'rb') as fd:  # pylint: disable=invalid-name
            return fd.read()

    def write(self, bs: bytes):
        with open(self.path, 'wb') as fd:  # pylint: disable=invalid-name
            fd.write(bs)

    def delete(self):
        raise NotImplementedError

    @classmethod
    def listdir(cls) -> Sequence[str]:
        raise NotImplementedError
