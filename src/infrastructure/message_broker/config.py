import os
from dataclasses import dataclass, field


@dataclass(frozen=True)
class EventBusConfig:
    host: str = "localhost"
    port: int = field(default_factory=lambda: int(os.environ.get("RMQ_PORT", 5672)))
    login: str = "admin"
    password: str = "admin"
