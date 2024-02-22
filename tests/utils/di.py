from pathlib import Path

from litestar import Litestar
from litestar.di import Provide

from src.infrastructure.config_loader import load_config
from src.infrastructure.db.config import DBConfig


def setup_test_di(app: Litestar, path: Path) -> None:
    db_config_data = load_config("db", path)
    db_config = DBConfig(**db_config_data)

    app.dependencies["db_config"] = Provide(
        lambda: db_config, sync_to_thread=False,
    )
