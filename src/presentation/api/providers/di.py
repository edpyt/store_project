from typing import AsyncGenerator

from di import ScopeState
from didiator.interface.utils.di_builder import DiBuilder

from src.infrastructure.di import DiScope


def get_di_state() -> ScopeState:
    raise NotImplementedError


def get_di_builder() -> DiBuilder:
    raise NotImplementedError


class StateProvider:
    def __init__(self, di_state: ScopeState | None = None) -> None:
        self._di_state = di_state

    async def build(
        self, di_builder: DiBuilder
    ) -> AsyncGenerator[ScopeState, None]:
        async with di_builder.enter_scope(DiScope):
            async with di_builder.enter_scope(
                DiScope.REQUEST, self._di_state
            ) as di_state:
                yield di_state
