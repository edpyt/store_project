from litestar import Litestar

from src.presentation.api.controllers.healthcheck import healthcheck_endpoint

from .product import ProductController


def setup_controllers(app: Litestar) -> None:
    app.register(healthcheck_endpoint)
    app.register(ProductController)
