from dataclasses import dataclass
from decimal import Decimal
from uuid import UUID

from didiator import EventMediator

from src.application.common.command import Command, CommandHandler
from src.application.common.interfaces.uow import UnitOfWork
from src.application.product.interfaces import ProductRepo
from src.domain.product.entities import Product
from src.domain.product.value_objects import ProductId, ProductProperty


@dataclass
class CreateProduct(Command[UUID]):
    product_id: UUID
    title: str
    price: Decimal
    weight: float


class CreateProductHandler(CommandHandler[CreateProduct, UUID]):
    def __init__(
        self,
        product_repo: ProductRepo,
        uow: UnitOfWork,
        mediator: EventMediator,
    ) -> None:
        self._product_repo = product_repo
        self._uow = uow
        self._mediator = mediator

    async def __call__(self, command: CreateProduct) -> UUID:
        product_id = ProductId(command.product_id)
        product_property = ProductProperty(
            command.title, command.price, command.weight
        )

        existing_product_properties = (
            await self._product_repo.get_existing_product_properties()
        )
        product = Product.create(
            product_id, product_property, existing_product_properties
        )
        await self._product_repo.add_product(product)
        await self._mediator.publish(product.pull_events())
        await self._uow.commit()

        return command.product_id
