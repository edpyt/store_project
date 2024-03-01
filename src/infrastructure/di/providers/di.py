from di import ScopeState
from didiator import Mediator
from didiator.interface.utils.di_builder import DiBuilder
from dishka import Provider, provide
from dishka.entities.component import Component
from dishka.entities.scope import BaseScope


@provide
class DiProvider(Provider):
    def __init__(
        self,
        mediator: Mediator,
        di_builder: DiBuilder,
        di_state: ScopeState | None,
        scope: BaseScope | None = None,
        component: Component | None = None,
    ):
        self.mediator = mediator
        self.di_builder = di_builder
        self.di_state = di_state
        super().__init__(scope, component)
