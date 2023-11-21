import logging

from .models import Job, Message
from .executor import AbstractExecutor


logger = logging.getLogger(__name__)


def execute(message: Message, executor: AbstractExecutor):
    """
    Execute the message by executor.
    """
    raise NotImplementedError


def start_job(job: Job) -> Message:
    """
    Start the job.
    """
    return Message(
        id=job.id,
        object=job.inputs,
        ticket=job.ticket,

        num=0,
        is_last=True,
    )
