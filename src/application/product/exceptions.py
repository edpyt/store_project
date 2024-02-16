from dataclasses import dataclass
from uuid import UUID

from src.application.common.exceptions import ApplicationError


@dataclass(eq=False)
class ProductIdAlreadyExistsError(ApplicationError):
    product_id: UUID

    @property
    def title(self) -> str:
        return "A product not exists"


@dataclass(eq=False)
class ProductIdNotExistError(ApplicationError):
    product_id: UUID

    @property
    def title(self) -> str:
        return f"Product with id {self.product_id} not exists"
