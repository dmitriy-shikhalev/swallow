import logging
import time

from .job import Job


logger = logging.getLogger(__name__)


SLEEP_TIME = 5


def main(job_path):
    """
    Main process.
    """
    job = Job(job_path)

    while not job.is_finished:
        job.beat()

    logger.info('Job is finished with status %s', job.status)
