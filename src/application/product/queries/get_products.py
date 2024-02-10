from src.application.common.query import QueryHandler
from src.application.product.dto import ProductDTO  # type: ignore[attr-defined]
from src.application.product.interfaces.persistence.reader import ProductReader


class GetProductsHandler(QueryHandler):
    def __init__(self, product_reader: ProductReader) -> None:
        self._product_reader = product_reader

    async def __call__(self) -> list[ProductDTO]:
        return await self._product_reader.get_products()
