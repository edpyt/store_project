import os
from pathlib import Path

import tomllib


def read_toml(path: Path) -> dict:
    f = path.open("rb")
    return tomllib.load(f)


def load_config(type_config: str, path: Path | None = None) -> dict:
    if path is None:
        path_str = os.environ["CONFIG_PATH"]
        path = Path(path_str)
    data = read_toml(path)
    return data[type_config]
