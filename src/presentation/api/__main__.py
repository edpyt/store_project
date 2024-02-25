import logging

from src.infrastructure.config_loader import load_config
from src.infrastructure.di import init_di_builder, setup_di_builder
from src.infrastructure.log import configure_logging

from .config import Config


async def main() -> None:
    config = load_config(Config)
    configure_logging(config.logging)

    logger = logging.getLogger(__name__)
    logger.info("Launch app")

    di_builder = init_di_builder()
    setup_di_builder(di_builder)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
