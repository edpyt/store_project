from pathlib import Path

import yaml


def read_config(config_path: Path) -> dict:
    with config_path.open('r') as c_file:
        return yaml.safe_load(c_file)
