from logging import Logger

from di import Container, ScopeState, bind_by_type
from di.dependent import Dependent
from di.executors import AsyncExecutor
from didiator import Mediator
from didiator.interface.utils.di_builder import DiBuilder
from didiator.utils.di_builder import DiBuilderImpl
from dishka import AsyncContainer, make_async_container

from src.application.common.interfaces.uow import UnitOfWork
from src.infrastructure.di.constants import DiScope
from src.infrastructure.di.factories import (
    setup_db_factories,
    setup_mediator_factories,
)
from src.infrastructure.di.factories.message_bus import (
    setup_event_bus_factories,
)
from src.infrastructure.di.providers import DiProvider, MediatorProvider, StateProvider
from src.infrastructure.log.main import build_logger
from src.infrastructure.mediator.utils import get_mediator
from src.infrastructure.uow import build_uow


def init_di_builder() -> DiBuilder:
    di_container = Container()
    di_executor = AsyncExecutor()
    di_scopes = [DiScope.APP, DiScope.REQUEST]
    di_builder = DiBuilderImpl(di_container, di_executor, di_scopes)
    return di_builder


def setup_di_builder(di_builder: DiBuilder) -> None:
    di_builder.bind(
        bind_by_type(
            Dependent(lambda *args: di_builder, scope=DiScope.APP), DiBuilder
        )
    )
    di_builder.bind(
        bind_by_type(Dependent(build_logger, scope=DiScope.APP), Logger)
    )
    di_builder.bind(
        bind_by_type(Dependent(build_uow, scope=DiScope.REQUEST), UnitOfWork)
    )
    setup_mediator_factories(di_builder, get_mediator, DiScope.REQUEST)
    setup_db_factories(di_builder)
    setup_event_bus_factories(di_builder)


def setup_container(
    mediator: Mediator,
    di_builder: DiBuilder,
    di_state: ScopeState | None = None,
) -> AsyncContainer:
    di_provider = DiProvider(
        mediator=mediator,
        di_builder=di_builder,
        di_state=di_state,
    )
    mediator_provider = MediatorProvider()
    state_provider = StateProvider()

    container = make_async_container(
        di_provider,
        mediator_provider,
        state_provider,
    )
    return container
