from pathlib import Path

from src.common.config.models.main import Config
from src.common.config.parser.config_reader import read_config
from src.infrastructure.db.config import DBConfig


def load_config(path: Path) -> Config:
    config: dict = read_config(path)

    db_config: DBConfig = DBConfig(**config)

    return Config(db_config)
