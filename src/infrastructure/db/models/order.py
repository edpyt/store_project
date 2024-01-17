from src.infrastructure.db.models.base import (
    BaseModelCreatedUpdated, BaseModelUUID
)


class Order(BaseModelUUID, BaseModelCreatedUpdated):
    __tablename__ = 'order'
