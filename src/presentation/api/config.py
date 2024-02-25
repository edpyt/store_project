from dataclasses import dataclass, field

from src.infrastructure.db import DBConfig
from src.infrastructure.log import LoggingConfig


@dataclass
class APIConfig:
    host: str = "127.0.0.1"
    port: int = 8000


@dataclass
class Config:
    db: DBConfig = field(default_factory=DBConfig)
    logging: LoggingConfig = field(default_factory=LoggingConfig)
    api: APIConfig = field(default_factory=APIConfig)
