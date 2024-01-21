
from sqlalchemy import Column

from sqlalchemy_utils import ChoiceType

from src.core.models.enums.order_status import Status
from src.infrastructure.db.models.base import (
    BaseModelCreatedUpdated, BaseModelUUID
)


class Order(BaseModelUUID, BaseModelCreatedUpdated):
    __tablename__ = 'order'

    status: Status = Column(
        ChoiceType(Status), nullable=False, default=Status.CREATED
    )
