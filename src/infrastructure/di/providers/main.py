from logging import Logger

from dishka import Provider, Scope, provide

from src.application.common.interfaces.uow import UnitOfWork
from src.infrastructure.db.uow import SQLAlchemyUOW
from src.infrastructure.log import build_logger
from src.infrastructure.message_broker.uow import RabbitMQUOW
from src.infrastructure.uow import build_uow


class MainProvider(Provider):
    logger = provide(build_logger, scope=Scope.APP, provides=Logger)

    @provide(scope=Scope.REQUEST)
    async def uow(self, db_uow: SQLAlchemyUOW, rq_uow: RabbitMQUOW) -> UnitOfWork:
        return build_uow(db_uow, rq_uow)
