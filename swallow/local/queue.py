import os
from datetime import datetime
from pathlib import Path

from ..domain.queue import AbstractQueue
from ..domain.models import Message
from .models import LocalFile


class LocalFolderQueue(AbstractQueue):  # pylint: disable=too-few-public-methods
    """
    Class for monitoring new files in local dir.
    """

    def __init__(self, dirname: Path):
        self.dirname = dirname

    def pop(self) -> Message | None:
        for filename in os.listdir(self.dirname):
            path = self.dirname / filename

            message = Message.from_file(
                LocalFile(path)
            )
            return message
        return None

    def append(self, message: Message):
        filename = str(message.id)
        timestamp = datetime.now().isoformat()
        filename = f'{timestamp}-{filename}.json'

        with open(self.dirname / filename, 'wb') as fd:  # pylint: disable=invalid-name
            fd.write(message.to_json())
