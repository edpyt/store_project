from decimal import Decimal

from src.domain.common.exceptions.base import DomainException


class ProductPropertyAlreadyExists(DomainException):
    product_property: tuple[str, float, Decimal] | None = None

    @property
    def title(self) -> str:
        if self.product_property is not None:
            return f'A product with property "{self.product_property}" already exists'
        else:
            return "A product with the product property already exists"
