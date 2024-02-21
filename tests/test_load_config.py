from pathlib import Path

from src.infrastructure.config_loader import load_config


async def test_load_config_data() -> None:
    config_test_path = Path(__file__).parent / "utils/config/test_config.toml"
    config_data = load_config("db", config_test_path)

    assert isinstance(config_data, dict)
