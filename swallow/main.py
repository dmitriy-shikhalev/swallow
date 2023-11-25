import atexit
import time
from argparse import ArgumentParser, Namespace

from .exceptions import UnknownExecutor, UnknownQueue, UnknownRepository
from .domain.executor import AbstractExecutor
from .domain.queue import AbstractQueue
from .domain.repository import AbstractRepository
from .local.executor import LocalExecutor
from .local.queue import InMemoryQueue
from .local.repository import SqliteRepository


SLEEP_TIME = 0.5


def get_settings() -> Namespace:
    """
    Settings of kc_auto script.
    """
    parser = ArgumentParser()
    parser.add_argument("name")
    parser.add_argument("--executor", dest='executor', required=True)
    parser.add_argument("--queue", dest='queue', required=True)
    parser.add_argument("--repository", dest='repository', required=True)

    return parser.parse_args()


def bootstrap() -> tuple[AbstractRepository, AbstractQueue, AbstractExecutor]:
    """
    Startup initialization function.
    """
    settings = get_settings()

    if settings.repository == 'SqliteRepository':
        repository = SqliteRepository(settings.name)
    else:
        raise UnknownRepository(settings.repository)

    if settings.queue == 'InMemoryQueue':
        queue = InMemoryQueue()
    else:
        raise UnknownQueue(settings.repository)

    if settings.executor == 'LocalExecutor':
        executor = LocalExecutor()
    else:
        raise UnknownExecutor(settings.executor)

    return repository, queue, executor


def shutdown():
    """
    Final everything at the end of process.
    """
    pass


def serve(repository: AbstractRepository, queue: AbstractQueue, executor: AbstractExecutor):
    """
    Infinite loop.
    """
    while True:
        message = queue.pull()
        if message is not None:
            if message.id is not None:
        else:
            time.sleep(SLEEP_TIME)


def main():
    """
    Main process.
    """
    repository, queue, executor = bootstrap()
    atexit.register(shutdown)

    serve(repository, queue, executor)
