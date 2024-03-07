from collections.abc import Sequence
from typing import Any


class Event:
    ...


class EventMediatorMock:
    def __init__(self) -> None:
        self.published_events: list[Event] = []

    async def publish(
        self, events: Event | Sequence[Event], *args: Any, **kwargs: Any
    ) -> None:
        if isinstance(events, Event):
            events = [events]
        self.published_events.extend(events)
