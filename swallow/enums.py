from enum import Enum

from .types import Int, Float, Str, List, Dict


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
    ONLY_ONE = 'ONLY_ONE'
    EVERY = 'EVERY'
    ALL = 'ALL'


class Type(Enum):
    """
    Enumeration of types of fields.
    """
    Int = Int
    Float = Float
    List = List
    Str = Str
    Dict = Dict
