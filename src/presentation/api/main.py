import logging

import uvicorn
from litestar import Litestar
from litestar.openapi import OpenAPIConfig

from src.presentation.api.controllers import setup_controllers
from src.presentation.api.di.main import setup_di
from src.presentation.api.exceptions.exc import all_exceptions_handler


def build_app() -> Litestar:
    return Litestar(
        on_startup=[setup_di, setup_controllers],
        exception_handlers={Exception: all_exceptions_handler},
        openapi_config=OpenAPIConfig(
            title="Simple Store Project",
            version="0.0.1",
            root_schema_site="swagger",
            enabled_endpoints={"swagger"},
        ),
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
