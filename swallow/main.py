import atexit
import time
from argparse import ArgumentParser, Namespace

from .domain.exceptions import UnknownExecutor, UnknownQueue, UnknownMonitor, UnknownRepository
from .domain.executor import AbstractExecutor
from .domain.queue import AbstractQueue
from .domain.monitor import AbstractMonitor
from .domain.repository import AbstractRepository
from .local.executor import LocalExecutor
from .local.queue import InMemoryQueue
from .local.monitor import LocalFolderMonitor
from .local.repository import SqliteRepository


SLEEP_TIME = 0.5


def get_settings() -> Namespace:
    """
    Settings of kc_auto script.
    """
    parser = ArgumentParser()
    parser.add_argument("name")
    parser.add_argument("folder")
    parser.add_argument("--executor", dest='executor', required=True)
    parser.add_argument("--queue", dest='queue', required=True)
    parser.add_argument("--repository", dest='repository', required=True)
    parser.add_argument("--monitor", dest='monitor', required=True)

    return parser.parse_args()


def bootstrap() -> tuple[AbstractRepository, AbstractQueue, AbstractExecutor, AbstractMonitor]:
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

    if settings.monitor == 'LocalFolderMonitor':
        monitor = LocalFolderMonitor(settings.folder)
    else:
        raise UnknownMonitor(settings.monitor)

    return repository, queue, executor, monitor


def shutdown():
    """
    Final everything at the end of process.
    """


def serve(repository: AbstractRepository, queue: AbstractQueue, executor: AbstractExecutor, monitor: AbstractMonitor):
    """
    Infinite loop.
    """
    while True:
        any_load = False

        new_file = monitor.get()
        if new_file is not None:
            any_load = True
            raise NotImplementedError

        message = queue.pull()
        if message is not None:
            any_load = True
            raise NotImplementedError

        if not any_load:
            time.sleep(SLEEP_TIME)


def main():
    """
    Main process.
    """
    repository, queue, executor, monitor = bootstrap()
    atexit.register(shutdown)

    serve(repository, queue, executor, monitor)
