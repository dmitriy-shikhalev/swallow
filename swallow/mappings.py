from sqlalchemy.orm import registry
from sqlalchemy.orm import relationship

from swallow.models import User, Address
from swallow.tables import user, address

mapper_registry = registry()


mapper_registry.map_imperatively(
    User,
    user,
    properties={
        "addresses": relationship(Address, backref="user", order_by=address.c.id),
    },
)

mapper_registry.map_imperatively(Address, address)
