from typing import AsyncGenerator

from aio_pika.abc import (
    AbstractChannel,
    AbstractConnection,
    AbstractTransaction,
)
from aio_pika.pool import Pool

from .config import EventBusConfig
from .factories import ChannelFactory, ConnectionFactory


def build_rq_connection_pool(
    event_bus_config: EventBusConfig,
) -> Pool[AbstractConnection]:
    rq_connection_pool = Pool(
        ConnectionFactory(event_bus_config).get_connection, max_size=10
    )
    return rq_connection_pool


def build_rq_channel_pool(
    rq_connection_pool: Pool[AbstractConnection],
) -> Pool[AbstractChannel]:
    rq_channel_pool = Pool(ChannelFactory(rq_connection_pool).get_channel, max_size=100)
    return rq_channel_pool


async def build_rq_channel(
    rq_channel_pool: Pool[AbstractChannel],
) -> AsyncGenerator[AbstractChannel, None]:
    async with rq_channel_pool.acquire() as channel:
        yield channel
        channel.transaction()


async def build_rq_transaction(
    rq_channel: AbstractChannel,
) -> AbstractTransaction:
    rq_transaction = rq_channel.transaction()
    await rq_transaction.select()
    return rq_transaction
