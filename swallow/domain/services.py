import logging
from dataclasses import replace

from .models import Job, JobStatus, Message
from .executor import AbstractExecutor
from .queue import AbstractQueue
from .repository import AbstractRepository


logger = logging.getLogger(__name__)


def execute(message: Message, executor: AbstractExecutor):
    """
    Execute the message by executor.
    """
    raise NotImplementedError


def start_job(job: Job, repository: AbstractRepository, queue: AbstractQueue):
    """
    Start the job.
    """
    queue.push(
        Message(
            id=job.id,
            object=job.inputs,
            ticket=job.ticket,
            num=0,
            is_last=True,
        )
    )

    new_job = replace(job, status=JobStatus.PROCESSING)
    repository.update(job.id, new_job)
