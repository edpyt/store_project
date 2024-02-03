from litestar import Litestar

from .routes import all_routes


def build_app() -> Litestar:
    return Litestar(all_routes)
