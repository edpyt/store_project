from typing import Annotated

from didiator import Mediator
from litestar import Controller, get, post
from litestar.di import Provide
from litestar.params import Dependency

from src.application.product.commands.create_product import CreateProduct
from src.application.product.dto.products import ProductDTO
from src.application.product.interfaces.persistence.reader import ProductReader
from src.presentation.api.controllers.responses.base import OkResponse
from src.presentation.api.di.product import create_product_reader_impl


class ProductController(Controller):  # type: ignore[misc]
    path = "/product"

    dependencies = {"product_reader": Provide(create_product_reader_impl)}  # noqa: RUF012

    @get("/all")  # type: ignore[misc]
    async def get_all_products(
        self,
        product_reader: Annotated[ProductReader, Dependency(skip_validation=True)],
    ) -> list[ProductDTO]:
        """Get all products endpoint.

        :param product_reader: ProductReader depends object
        """
        return await product_reader.get_products()

    @post("/create/", status_code=200)  # type: ignore[misc]
    async def create_product(  # type: ignore[empty-body]
        self,
        create_product_command: CreateProduct,
        mediator: Annotated[Mediator, Dependency(skip_validation=True)]
    ) -> OkResponse:
        """Create product endpoint.

        :param product: Product DTO object
        :param product_reader: ProductReader depends object
        """
        product_id = await mediator.send(create_product_command)
        product = await mediator.query(GetProductById(product_id=product_id))
        return OkResponse(product, status_code=201)
