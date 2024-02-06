from litestar import Litestar
from litestar.di import Provide

from src.application.common.config.parser.main import load_config


def setup_test_di(app: Litestar, path: str) -> None:
    app.dependencies["db_config"] = Provide(
        lambda: load_config(path, type_config="db"), sync_to_thread=False
    )
