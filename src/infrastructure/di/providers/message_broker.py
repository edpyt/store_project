from typing import AsyncGenerator

from aio_pika.abc import AbstractChannel, AbstractConnection, AbstractTransaction
from aio_pika.pool import Pool
from dishka import Provider, Scope, provide

from src.infrastructure.message_broker.config import EventBusConfig
from src.infrastructure.message_broker.main import (
    build_rq_channel,
    build_rq_channel_pool,
    build_rq_connection_pool,
    build_rq_transaction,
)


class MessageBrokerProvider(Provider):
    @provide(scope=Scope.APP)
    async def rq_connection_pool(
        self, event_bus_config: EventBusConfig
    ) -> AsyncGenerator[Pool[AbstractConnection], None]:
        rq_pool = build_rq_connection_pool(event_bus_config)
        async with rq_pool:
            yield rq_pool

    @provide(scope=Scope.APP)
    async def rq_channel_pool(
        self, rq_connection_pool: Pool[AbstractConnection]
    ) -> AsyncGenerator[Pool[AbstractChannel], None]:
        channel_pool = build_rq_channel_pool(rq_connection_pool)
        async with channel_pool:
            yield channel_pool

    @provide(scope=Scope.REQUEST)
    async def rq_channel(
        self, rq_channel_pool: Pool[AbstractChannel]
    ) -> AsyncGenerator[AbstractChannel, None]:
        yield await anext(build_rq_channel(rq_channel_pool))

    @provide(scope=Scope.REQUEST)
    async def rq_transaction(self, rq_channel: AbstractChannel) -> AbstractTransaction:
        return await build_rq_transaction(rq_channel)
