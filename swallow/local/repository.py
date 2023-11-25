import sqlite3
from dataclasses import asdict
from typing import Any

from ..domain.models import Job, JobID
from ..domain.repository import AbstractRepository


class SqliteRepository(AbstractRepository):
    """
    Class SQLite repository.
    """
    def __init__(self, name: str):
        self.name = name
        self.connection = sqlite3.connect(name)  # pylint: disable=invalid-name

        self.init_db()

    def init_db(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute("""
                        CREATE TABLE jobs(
                           id TEXT primary key,
                           ticket TEXT,
                           inputs TEXT,
                           outputs TEXT,
                           status TEXT
                        )
                    """)
        finally:
            cursor.close()

    def create(self, job: Job) -> Any:
        cursor = self.connection.cursor()
        try:
            cursor.execute("""
                INSERT INTO jobs (id, ticket, inputs, outputs, status)
                    VALUES (:id, :ticket, :inputs, :outputs, :status)
            """, asdict(job))
        finally:
            cursor.close()

    def get(self, pk: Any) -> Job:
        raise NotImplementedError

    def update(self, pk: Any, job: Job):
        raise NotImplementedError

    def delete(self, pk: JobID):
        raise NotImplementedError
