import os
from .enums import Status

import yaml


class Job:
    status: Status

    def __init__(self, job_path: str):
        self.job_path = job_path
        self.initialize()

    def initialize(self):
        path = os.path.join(self.job_path, "main.yaml")

        job_data = yaml.load(
            open(path, "r"), Loader=yaml.FullLoader
        )
        self.status = job_data.get("status", Status.NEW)

    @property
    def is_finished(self):
        return self.status in (
            Status.DONE,
            Status.ERROR,
        )

    def beat(self):
        if self.status == Status.NEW:
            self.init_steps()

        if self.status == Status.PROCESSING:
            self.work()
