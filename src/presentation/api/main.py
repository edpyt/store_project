from litestar import Litestar

from src.presentation.api.routes import setup_routes


def build_app() -> Litestar:
    app = Litestar()
    setup_routes(app)

    return app
