import logging

from litestar import Litestar
import uvicorn

from src.infrastructure.di.main import setup_di
from src.presentation.api.routes import setup_routes


def build_app() -> Litestar:
    app = Litestar()

    setup_di(app)
    setup_routes(app)

    return app


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
