from ..domain.models import Aggregate, AggregateKey, Message
from ..domain.repository import AbstractRepository


class RedisRepository(AbstractRepository):
    """
    Redis repository.
    """
    def __init__(self, redis_url: str) -> None:
        raise NotImplementedError

    def create(self, key: AggregateKey):
        raise NotImplementedError

    def get(self, key: AggregateKey) -> Aggregate:
        raise NotImplementedError

    def delete(self, key: AggregateKey):
        raise NotImplementedError

    def add(self, key: AggregateKey, message: Message):
        raise NotImplementedError
