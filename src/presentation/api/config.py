from dataclasses import dataclass, field

from src.infrastructure.db import DBConfig


@dataclass
class APIConfig:
    host: str = "127.0.0.1"
    port: int = 8000


@dataclass
class Config:
    db: DBConfig = field(default_factory=DBConfig)
