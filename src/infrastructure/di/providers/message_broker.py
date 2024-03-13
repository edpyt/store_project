from aio_pika.abc import AbstractChannel, AbstractConnection, AbstractTransaction
from aio_pika.pool import Pool
from dishka import Provider, Scope, provide

from src.infrastructure.message_broker.main import (
    build_rq_channel,
    build_rq_channel_pool,
    build_rq_connection_pool,
    build_rq_transaction,
)


class MessageBrokerProvider(Provider):
    rq_connection_pool = provide(
        build_rq_connection_pool, scope=Scope.APP, provides=Pool[AbstractConnection]
    )
    rq_channel_pool = provide(
        build_rq_channel_pool, scope=Scope.APP, provides=Pool[AbstractChannel]
    )
    rq_channel = provide(
        build_rq_channel, scope=Scope.REQUEST, provides=AbstractChannel
    )
    rq_transaction = provide(
        build_rq_transaction, scope=Scope.REQUEST, provides=AbstractTransaction
    )
