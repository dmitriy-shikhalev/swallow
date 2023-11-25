from ..domain.queue import AbstractQueue
from ..domain.models import Message


class InMemoryQueue(AbstractQueue):
    """
    Local queue.
    """
    storage: list[Message]

    def __init__(self):
        self.storage = []

    def push(self, message: Message):
        self.storage.append(message)

    def pull(self) -> Message | None:
        try:
            return self.storage.pop()
        except IndexError:
            return None
