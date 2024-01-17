from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import MetaData, sql
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_N_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_N_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}


class BaseModel(DeclarativeBase):
    """Base SQLAlchemy model"""

    metadata: MetaData = MetaData(naming_convention=convention)


class BaseModelUUID(BaseModel):
    """Base model with uuid primary key field"""

    __abstract__ = True

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)


class BaseModelCreatedUpdated(BaseModel):
    """Base model with timestamp created and updated fields"""

    __abstract__ = True

    created_at: Mapped[datetime] = mapped_column(
        nullable=False, server_default=sql.func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        nullable=False, server_default=sql.func.now(), onupdate=sql.func.now()
    )
