from typing import Sequence

from src.application.common.interfaces.uow import UnitOfWork
from src.infrastructure.db.uow import SQLAlchemyUOW
from src.infrastructure.message_broker.uow import RabbitMQUOW


def build_uow(db_uow: SQLAlchemyUOW, rq_uow: RabbitMQUOW) -> UnitOfWork:
    uow = UnitOfWorkImpl([db_uow, rq_uow])
    return uow


class UnitOfWorkImpl(UnitOfWork):
    def __init__(self, uows: Sequence[UnitOfWork]) -> None:
        self._uows = uows

    async def commit(self) -> None:
        for uow in self._uows:
            await uow.commit()

    async def rollback(self) -> None:
        for uow in self._uows:
            await uow.rollback()
