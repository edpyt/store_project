from di import ScopeState
from didiator import Mediator
from didiator.interface.utils.di_builder import DiBuilder
from dishka import make_async_container
from dishka.integrations.litestar import setup_dishka
from litestar import Litestar

from src.infrastructure.di.providers import (
    DiProvider,
    MediatorProvider,
    StateProvider,
)


def setup_providers(
    app: Litestar,
    mediator: Mediator,
    di_builder: DiBuilder,
    di_state: ScopeState | None = None,
) -> None:
    di_provider = DiProvider(
        mediator=mediator,
        di_builder=di_builder,
        di_state=di_state,
    )
    mediator_provider = MediatorProvider()
    state_provider = StateProvider()

    container = make_async_container(
        di_provider, mediator_provider, state_provider,
    )
    setup_dishka(container, app)
