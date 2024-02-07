from litestar import Litestar

from .product import ProductController


def setup_controllers(app: Litestar) -> None:
    app.register(ProductController)
