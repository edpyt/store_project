from pathlib import Path

import tomllib


def read_toml(path: Path) -> dict:
    with open(path, "rb") as f:
        return tomllib.load(f)
