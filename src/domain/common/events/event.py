from abc import ABC
from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4


@dataclass(frozen=True)
class Event(ABC):
    event_id: UUID = field(init=False, kw_only=True, default_factory=uuid4)
    event_timestamp: datetime = field(
        init=False, kw_only=True, default_factory=datetime.utcnow
    )
