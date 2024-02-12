from pathlib import Path
from typing import Any

import yaml


def read_config(config_path: Path) -> Any:  # noqa: ANN401
    with config_path.open("r") as c_file:
        return yaml.safe_load(c_file)
