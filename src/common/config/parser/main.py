from pathlib import Path
from typing import Literal

from src.common.config.models.main import Config
from src.common.config.parser.config_reader import read_config
from src.infrastructure.db.config import DBConfig


def load_config(
    path: str | None = None, type_config: Literal['all', 'db'] = 'all'
) -> Config | DBConfig:
    if path is None:
        path = './config_dist/config.yml'
    path_obj = Path(path)

    config: dict = read_config(path_obj)
    db_config: DBConfig = DBConfig(**config)

    config: Config = Config(db_config)

    match type_config:
        case 'db':
            return db_config
        case _:
            return config
