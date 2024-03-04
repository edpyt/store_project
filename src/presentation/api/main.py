from dishka import AsyncContainer
from dishka.integrations.litestar import setup_dishka
from litestar import Litestar
from litestar.openapi import OpenAPIConfig
from litestar.plugins.structlog import StructlogPlugin

from src.infrastructure.config_loader import load_config
from src.infrastructure.di import init_di_builder, setup_container, setup_di_builder
from src.infrastructure.di.constants import DiScope
from src.infrastructure.event_bus.exchanges import declare_exchanges
from src.infrastructure.log import configure_logging
from src.infrastructure.mediator import init_mediator, setup_mediator
from src.presentation.api.controllers import setup_controllers

from .config import Config, setup_di_builder_config
from .docs import StoreProjectOpenAPIController


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

    di_builder = init_di_builder()
    setup_di_builder(di_builder)
    setup_di_builder_config(di_builder, config)

    async with di_builder.enter_scope(DiScope.APP) as di_state:
        mediator = await di_builder.execute(
            init_mediator, DiScope.APP, state=di_state
        )
        setup_mediator(mediator)

        async with di_builder.enter_scope(
            DiScope.REQUEST, state=di_state
        ) as req_di_state:
            await di_builder.execute(
                declare_exchanges, DiScope.REQUEST, state=req_di_state
            )

        container: AsyncContainer = setup_container(mediator, di_builder, di_state)
        setup_dishka(container, app)
