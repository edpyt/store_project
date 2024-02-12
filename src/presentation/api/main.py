import logging

import uvicorn
from litestar import Litestar

from src.presentation.api.di.main import setup_di
from src.presentation.api.exceptions.exc import all_exceptions_handler
from src.presentation.api.routes import setup_controllers


def build_app() -> Litestar:
    return Litestar(
        on_startup=[setup_di, setup_controllers],
        exception_handlers={Exception: all_exceptions_handler},
    )


async def run_app(app: Litestar) -> None:
    config = uvicorn.Config(
        app=app,
        host="0.0.0.0",
        port=8000,
        log_level=logging.INFO,
        log_config=None,
    )
    server = uvicorn.Server(config)
    await server.serve()
