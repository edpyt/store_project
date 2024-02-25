import aio_pika
from di import bind_by_type
from di.dependent import Dependent
from didiator.interface.utils.di_builder import DiBuilder

from src.infrastructure.di.constants import DiScope
from src.infrastructure.message_broker.main import (
    build_rq_channel,
    build_rq_channel_pool,
    build_rq_connection_pool,
    build_rq_transaction,
)


def setup_event_bus_factories(di_builder: DiBuilder) -> None:
    di_builder.bind(
        bind_by_type(
            Dependent(build_rq_connection_pool, scope=DiScope.REQUEST),
            aio_pika.pool.Pool[aio_pika.abc.AbstractConnection],
        ),
    )
    di_builder.bind(
        bind_by_type(
            Dependent(build_rq_channel_pool, scope=DiScope.APP),
            aio_pika.pool.Pool[aio_pika.abc.AbstractChannel],
        )
    )
    di_builder.bind(
        bind_by_type(
            Dependent(build_rq_channel, scope=DiScope.REQUEST),
            aio_pika.abc.AbstractChannel,
        )
    )
    di_builder.bind(
        bind_by_type(
            Dependent(build_rq_transaction, scope=DiScope.REQUEST),
            aio_pika.abc.AbstractTransaction,
        )
    )
