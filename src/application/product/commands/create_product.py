from dataclasses import dataclass
from decimal import Decimal
from uuid import UUID

from src.application.common.command import Command, CommandHandler
from src.application.common.interfaces.uow import UnitOfWork
from src.application.product.interfaces import ProductRepo
from src.domain.product.value_objects import Price, ProductId, Title, Weight


@dataclass
class CreateProduct(Command[UUID]):
    product_id: UUID
    title: str
    price: Decimal
    weight: float


class CreateProductHandler(CommandHandler[CreateProduct, UUID]):
    def __init__(self, product_repo: ProductRepo, uow: UnitOfWork) -> None:
        self._product_repo = product_repo
        self._uow = uow

    async def __call__(self, command: CreateProduct) -> None:
        product_id = ProductId(command.product_id)  # noqa: F841
        title = Title(command.title)  # noqa: F841
        price = Price(command.price)  # noqa: F841
        weight = Weight(command.weight)  # noqa: F841
