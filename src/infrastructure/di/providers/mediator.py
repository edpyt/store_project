from typing import Any

from di import ScopeState
from didiator import Mediator
from dishka import Provider, provide

from src.infrastructure.mediator import get_mediator


class MediatorProvider(Provider):
    @provide
    async def build(self, mediator: Mediator, di_state: ScopeState) -> Mediator:
        di_values: dict[Any, Any] = {ScopeState: di_state}
        mediator = mediator.bind(di_state=di_state, di_values=di_values)
        di_values |= {get_mediator: mediator}
        return mediator
