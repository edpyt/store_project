from di import ScopeState
from didiator import Mediator
from didiator.interface.utils.di_builder import DiBuilder
from dishka import Provider, Scope


class DiProvider(Provider):
    scope = Scope.APP

    def __init__(
        self,
        mediator: Mediator,
        di_builder: DiBuilder,
        di_state: ScopeState | None,
    ):
        super().__init__()
        self.mediator = mediator
        self.di_builder = di_builder
        self.di_state = di_state
