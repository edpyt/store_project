from typing import AsyncGenerator

from di import ScopeState
from didiator.interface.utils.di_builder import DiBuilder
from dishka import Provider, provide

from src.infrastructure.di import DiScope


class StateProvider(Provider):
    @provide
    async def build(
        self, di_state: ScopeState | None, di_builder: DiBuilder
    ) -> AsyncGenerator[ScopeState, None]:
        async with di_builder.enter_scope(DiScope):
            async with di_builder.enter_scope(
                DiScope.REQUEST, di_state
            ) as di_state:
                yield di_state
