from pathlib import Path

from src.infrastructure.config_loader import load_config
from src.presentation.api.config import Config


async def test_load_config_data() -> None:
    config_test_path = Path(__file__).parent / "utils/config/test_config.toml"
    config = load_config(Config, path=str(config_test_path))

    assert isinstance(config, Config)
