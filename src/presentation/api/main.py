import logging

import uvicorn
from di import ScopeState
from didiator import Mediator
from didiator.interface.utils.di_builder import DiBuilder
from litestar import Litestar
from litestar.openapi import OpenAPIConfig

from src.presentation.api.controllers import setup_controllers
from src.presentation.api.exceptions.exc import all_exceptions_handler
from src.presentation.api.providers.main import setup_providers

from .config import APIConfig


def init_api(
    mediator: Mediator,
    di_builder: DiBuilder,
    di_state: ScopeState | None = None,
) -> Litestar:
    # TODO: add logger
    app = Litestar(
        on_startup=[
            lambda ready_app: setup_providers(
                ready_app, mediator, di_builder, di_state
            ),
            setup_controllers,
        ],
        exception_handlers={Exception: all_exceptions_handler},
        openapi_config=OpenAPIConfig(
            title="Simple Store Project",
            version="0.0.1",
            root_schema_site="swagger",
            enabled_endpoints={"swagger"},
        ),
    )
    return app


async def run_app(app: Litestar, api_config: APIConfig) -> None:
    config = uvicorn.Config(
        app=app,
        host=api_config.host,
        port=api_config.port,
        log_level=logging.INFO,
        log_config=None,
    )
    server = uvicorn.Server(config)
    await server.serve()
