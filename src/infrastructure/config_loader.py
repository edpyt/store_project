import os
from pathlib import Path
from typing import TypeVar

import tomllib

from src.infrastructure.db.config import DBConfig
from src.infrastructure.log.config import LoggingConfig

T = TypeVar("T")


def read_toml(path: str) -> dict:
    with open(path, "rb") as f:
        toml_data = tomllib.load(f)
    return toml_data


def load_config(
    config_type: type[T],
    config_scope: str | None = None,
    path: str | None = None,
) -> T:
    if path is None:
        path = os.getenv("CONFIG_PATH", "./config/config.toml")
    data = read_toml(path)
    if config_scope is not None:
        data = data[config_scope]
    else:
        data["db"] = DBConfig(**data["db"])
        if log_path := data["logging"].get("path"):
            data["logging"]["path"] = Path(log_path)
        data["logging"] = LoggingConfig(**data["logging"])
    return config_type(**data)
