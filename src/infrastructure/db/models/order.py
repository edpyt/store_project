from src.infrastructure.db.models.base import BaseModelCreatedUpdated


class Order(BaseModelCreatedUpdated):
    __tablename__ = 'order'
