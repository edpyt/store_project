from litestar import Litestar
from litestar.di import Provide

from src.presentation.api.config.parser import load_config
from src.presentation.api.di.db import build_async_engine, db_async_session
from src.presentation.api.di.product import create_product_reader_impl


def setup_di(app: Litestar) -> None:  # noqa: ARG001
    db_config_dependency = Provide(
        lambda: load_config(type_config="db"),
        sync_to_thread=False,
    )

    app.dependencies.setdefault("db_config", db_config_dependency)
    app.dependencies["engine"] = Provide(build_async_engine)
    app.dependencies["session"] = Provide(db_async_session)

    app.dependencies["product_reader"] = Provide(create_product_reader_impl)