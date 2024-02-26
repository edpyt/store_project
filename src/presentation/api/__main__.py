import logging

from src.infrastructure.config_loader import load_config
from src.infrastructure.di import init_di_builder, setup_di_builder
from src.infrastructure.di.constants import DiScope
from src.infrastructure.log import configure_logging
from src.infrastructure.mediator import init_mediator, setup_mediator
from src.presentation.api.main import init_api, run_app

from .config import Config, setup_di_builder_config


async def main() -> None:
    config = load_config(Config)
    configure_logging(config.logging)

    logger = logging.getLogger(__name__)
    logger.info("Launch app")

    di_builder = init_di_builder()
    setup_di_builder(di_builder)
    setup_di_builder_config(di_builder, config)

    async with di_builder.enter_scope(DiScope.APP) as di_state:
        mediator = await di_builder.execute(init_mediator, DiScope.APP, state=di_state)
        setup_mediator(mediator)

        app = init_api(logger, mediator, di_builder, di_state)
        await run_app(app, config.api)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
