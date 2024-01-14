from dataclasses import dataclass

from src.infrastructure.db.config import DBConfig


@dataclass
class Config:
    db: DBConfig
