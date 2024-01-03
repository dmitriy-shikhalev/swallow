import atexit
import logging

from .bootstrap import bootstrap
from .domain.services import serve


logger = logging.getLogger(__name__)


def shutdown():
    """
    Final everything at the end of process.
    """


def main():
    """
    Main process.
    """
    queue, repository = bootstrap()
    atexit.register(shutdown)

    serve(queue, repository)
