from .config import Config


async def main() -> None:
    config = load_config(Config)
