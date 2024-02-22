from src.infrastructure.config_loader import load_config
from src.infrastructure.di import init_di_builder, setup_di_builder


async def main() -> None:
    config = load_config("db")  # noqa: F841

    di_builder = init_di_builder()
    setup_di_builder(di_builder)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
