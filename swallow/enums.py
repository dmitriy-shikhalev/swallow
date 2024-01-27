from enum import Enum


class Status(Enum):
    """
    Enumeration of possible statuses of job.
    """
    NEW = 'NEW'
    PROCESSING = 'PROCESSING'
    ERROR = 'ERROR'
    DONE = 'DONE'


class Resistor(Enum):
    """
    Enumeration of possible types of resisting of datas.
    """
    ONE = 'ONE'
    EVERY = 'EVERY'
    ALL = 'ALL'
