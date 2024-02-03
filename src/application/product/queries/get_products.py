from src.application.common.query import QueryHandler
from src.application.product import dto
from src.application.product.interfaces.persistence.reader import ProductReader


class GetProductsHandler(QueryHandler):
    def __init__(self, product_reader: ProductReader) -> None:
        self._product_reader = product_reader

    async def __call__(self) -> list[dto.Product]:
        return await self._product_reader.get_products()
