from litestar import Litestar
from litestar.di import Provide

from src.application.common.config.parser.main import load_config
from src.infrastructure.db.main import build_async_engine, db_async_session


def setup_di(app: Litestar) -> None:  # noqa: ARG001
    app.dependencies["db_config"] = Provide(
        lambda: load_config(type_config="db"),
        sync_to_thread=False,
    )
    app.dependencies["engine"] = Provide(build_async_engine)
    app.dependencies["session"] = Provide(db_async_session)
