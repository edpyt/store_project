from pathlib import Path
from typing import Any, Literal

from src.infrastructure.db.config import DBConfig
from src.presentation.api.config.models.main import Config
from src.presentation.api.config.parser.config_reader import read_config


def load_config(
    path: str | None = None,
    type_config: Literal["all", "db"] = "all",
) -> Config | DBConfig:
    if path is None:
        path = "./config_dist/dev_config.yml"
    path_obj = Path(path)

    config_data: dict[str, dict[str, Any]] = read_config(path_obj)
    db_config: DBConfig = DBConfig(**config_data["db"])

    config: Config = Config(db=db_config)

    match type_config:
        case "db":
            return db_config
        case _:
            return config
