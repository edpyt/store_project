from datetime import datetime

from sqlalchemy import sql
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class BaseModel(DeclarativeBase):
    """Base SQLAlchemy model"""
    ...


class BaseModelCreatedUpdated(BaseModel):
    """Base model with timestamp created and updated fields"""

    __abstract__ = True

    created_at: Mapped[datetime] = mapped_column(
        nullable=False, server_default=sql.func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        nullable=False, server_default=sql.func.now(), onupdate=sql.func.now()
    )
