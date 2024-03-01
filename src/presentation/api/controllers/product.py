from typing import Annotated

from didiator import Mediator
from dishka.integrations.litestar import Depends
from litestar import Controller, Response, get, post

from src.application.product.commands.create_product import CreateProduct
from src.application.product.dto.products import ProductDTO
from src.application.product.interfaces.persistence.reader import ProductReader


class ProductController(Controller):  # type: ignore[misc]
    path = "/product"
    tags = ["Product"]

    @get(
        "/all",
        summary="GET products",
        description="Get all products from database.",
    )  # type: ignore[misc]
    async def get_all_products(
        self,
        product_reader: Annotated[ProductReader, Depends()],
    ) -> list[ProductDTO]:
        """Get all products endpoint.

        :param product_reader: ProductReader depends object
        """
        return await product_reader.get_products()

    @post(
        "/create/",
        summary="CREATE product",
        description="Create product in database.",
        status_code=201,
    )  # type: ignore[misc]
    async def create_product(  # type: ignore[empty-body]
        self,
        create_product_command: CreateProduct,
        mediator: Annotated[Mediator, Depends()],
    ) -> Response:
        """Create product endpoint.

        :param product: Product DTO object
        :param product_reader: ProductReader depends object
        """
        product_id = await mediator.send(create_product_command)
        product = product_id
        # product = await mediator.query(GetProductById(product_id=product_id))
        return Response(product, status_code=201)
