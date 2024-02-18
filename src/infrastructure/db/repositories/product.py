from decimal import Decimal
from typing import Iterable, NoReturn

from sqlalchemy import select
from sqlalchemy.exc import DBAPIError, IntegrityError

from src.application.common.exceptions import RepoError
from src.application.product.dto import ProductDTO
from src.application.product.exceptions import (
    ProductIdAlreadyExistsError,  # type: ignore[attr-defined]
)
from src.application.product.interfaces import ProductReader, ProductRepo
from src.domain.product import entities
from src.domain.product.value_objects import ProductProperty
from src.infrastructure.db.converters import convert_product_entity_to_db_model
from src.infrastructure.db.exception_mapper import exception_mapper
from src.infrastructure.db.models.product import Product
from src.infrastructure.db.repositories.base import SQLAlchemyRepo


class ProductReaderImpl(SQLAlchemyRepo, ProductReader):
    async def get_products(self) -> list[ProductDTO]:
        stmt = select(Product)
        result = await self._session.scalars(stmt)
        return [
            ProductDTO(
                title=product.title,
                price=product.price,
                weight=product.weight,
            )
            for product in result.all()
        ]


class ProductRepoImpl(SQLAlchemyRepo, ProductRepo):
    @exception_mapper
    async def get_existing_product_properties(self) -> set[ProductProperty]:
        result: Iterable[
            tuple[str, float, Decimal]
        ] = await self._session.scalars(
            select(Product.title, Product.weight, Product.price)
        )
        existing_products = {
            ProductProperty(title=title, weight=weight, price=price)
            for title, weight, price in result
        }
        return existing_products

    @exception_mapper
    async def add_product(self, product: entities.Product) -> None:
        db_product = convert_product_entity_to_db_model(product)
        try:
            await self._session.merge(db_product)
        except IntegrityError as err:
            self._parse_error(err, product)

    def _parse_error(self, err: DBAPIError, product: entities.Product) -> NoReturn:
        match err.__cause__.__cause__.constraint_name:  # type: ignore
            case "pk_product":
                raise ProductIdAlreadyExistsError(product.id.to_raw()) from err
            case _:
                raise RepoError from err
