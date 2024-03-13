from dishka import make_async_container
from dishka.integrations.litestar import setup_dishka
from litestar import Litestar
from litestar.openapi import OpenAPIConfig
from litestar.plugins.structlog import StructlogPlugin

from src.infrastructure.config_loader import load_config
from src.infrastructure.di import setup_providers
from src.infrastructure.log import configure_logging
from src.presentation.api.controllers import setup_controllers
from src.presentation.api.controllers.docs import StoreProjectOpenAPIController

from .config import Config, setup_di_config


def init_api() -> Litestar:
    app = Litestar(
        on_startup=[
            setup_app,
            setup_controllers,
        ],
        openapi_config=OpenAPIConfig(
            title="Simple Store Project",
            version="0.0.1",
            root_schema_site="swagger",
            enabled_endpoints={"swagger"},
            openapi_controller=StoreProjectOpenAPIController,
        ),
        plugins=[StructlogPlugin()],
    )
    app.logger.info("Start application")
    return app


async def setup_app(app: Litestar) -> None:
    config = load_config(Config)
    configure_logging(config.logging)

    di_providers = setup_providers()
    setup_di_config(config, di_providers.main)

    di_container = make_async_container(*di_providers)
    setup_dishka(di_container, app)
