import logging
from dataclasses import replace  # pylint: disable=unused-import
from random import shuffle
from typing import Generator

from .queue import AbstractQueue
from .models import Message
from .repository import AbstractRepository



logger = logging.getLogger(__name__)


def execute(message: Message):
    """
    Execute the message by executor.
    """
    raise NotImplementedError


def generator(*queues: AbstractQueue) -> Generator[Message, None, None]:
    """"
    Function for lister several queues.
    """
    mutable_list_queues = list(queues)
    shuffle(mutable_list_queues)
    while True:
        for queue in mutable_list_queues:
            message = queue.pop()

            if message:
                yield message


def serve(queue: AbstractQueue, repository: AbstractRepository) -> None:
    """
    Infinite loop.
    """
    queue_generator = generator(queue)

    for message in queue_generator:
        logger.info('Get new message: %s', message)
        execute(message)
