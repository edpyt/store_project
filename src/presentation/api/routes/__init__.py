from litestar import Litestar

from .product import get_all_products


def setup_routes(app: Litestar) -> None:
    app.register(get_all_products)
