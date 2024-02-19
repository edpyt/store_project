from dataclasses import dataclass, field

from src.infrastructure.db import DBConfig


@dataclass
class Config:
    db: DBConfig = field(default_factory=DBConfig)
