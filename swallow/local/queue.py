import os
from datetime import datetime
from pathlib import Path
from uuid import uuid4

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

            local_file = LocalFile(path=path)

            message = Message.from_file(local_file)
            local_file.delete()
            return message
        return None

    def append(self, message: Message):
        filename = uuid4().hex
        timestamp = datetime.now().isoformat()
        filename = f'{timestamp}-{filename}.json'
        local_file = LocalFile(Path(filename))

        local_file.write(message.to_json())
