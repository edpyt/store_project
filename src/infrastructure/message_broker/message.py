from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass(frozen=True, kw_only=True)
class Message:
    id: UUID = field(default_factory=uuid4)
    data: str = ""
    message_type: str = "message"
