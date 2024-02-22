from di import ScopeState
from didiator import Mediator
from didiator.interface.utils.di_builder import DiBuilder
from litestar import Litestar

from src.presentation.api.providers.di import StateProvider
from src.presentation.api.providers.mediator import MediatorProvider


def setup_providers(
    app: Litestar,
    mediator: Mediator,
    di_builder: DiBuilder,
    di_state: ScopeState | None = None,
) -> None:
    mediator_provider = MediatorProvider(mediator)

    app.dependencies["mediator"] = mediator_provider.build

    state_provider = StateProvider(di_state)

    app.dependencies["di_builder"] = lambda: di_builder
    app.dependencies["di_state"] = state_provider.build
