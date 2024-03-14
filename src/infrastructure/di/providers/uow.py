from dishka import Provider, Scope, provide

from src.infrastructure.db.uow import SQLAlchemyUOW
from src.infrastructure.message_broker.uow import RabbitMQUOW


class UOWProvider(Provider):
    db_uow = provide(SQLAlchemyUOW, scope=Scope.REQUEST)
    rmq_uow = provide(RabbitMQUOW, scope=Scope.REQUEST)
