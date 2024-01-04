from .domain.queue import AbstractQueue
from .domain.repository import AbstractRepository
from .local.queue import LocalFolderQueue
from .local.repository import RedisRepository
from .settings import get_settings


def bootstrap() -> tuple[AbstractQueue, AbstractRepository]:
    """
    Startup initialization function.
    """
    settings = get_settings()

    queue = LocalFolderQueue(settings.dirname)
    repository = RedisRepository(settings.redis_url)

    return queue, repository
