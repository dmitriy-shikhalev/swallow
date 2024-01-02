import atexit
import logging
import time
from argparse import ArgumentParser, Namespace

from .domain.queue import AbstractQueue
from .domain.repository import AbstractRepository
from .domain.services import execute, generator
from .local.queue import LocalFolderQueue


logger = logging.getLogger(__name__)


SLEEP_TIME = 0.5


class UnknownArgumentValue(Exception):
    """
    Exception for unknown argument value.
    """


def get_settings() -> Namespace:
    """
    Settings of kc_auto script.
    """
    parser = ArgumentParser()
    parser.add_argument("name")
    parser.add_argument("dirname")
    parser.add_argument("--queue", dest='queue', required=True)

    return parser.parse_args()


def bootstrap() -> tuple[AbstractRepository, AbstractQueue]:
    """
    Startup initialization function.
    """
    settings = get_settings()

    if settings.queue == 'LocalFolderQueue':
        queue = LocalFolderQueue(settings.indir)
    else:
        raise UnknownArgumentValue(settings.monitor)

    return queue


def shutdown():
    """
    Final everything at the end of process.
    """


def serve(queue: AbstractQueue):
    """
    Infinite loop.
    """
    queue_generator = generator(queue)

    for message in queue_generator:
        logger.info('Get new messsage: %s', message)
        execute(message)


def main():
    """
    Main process.
    """
    repository, queue = bootstrap()
    atexit.register(shutdown)

    serve(repository, queue)
