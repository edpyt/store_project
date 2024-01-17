from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.db.models.base import (
    BaseModelCreatedUpdated, BaseModelUUID
)


class Product(BaseModelUUID, BaseModelCreatedUpdated):
    __tablename__ = 'product'

    name: Mapped[str] = mapped_column(String(255))
