from litestar import Litestar

from src.infrastructure.di.main import setup_di
from src.presentation.api.routes import setup_routes


def build_app() -> Litestar:
    app = Litestar()

    setup_di(app)
    setup_routes(app)

    return app
