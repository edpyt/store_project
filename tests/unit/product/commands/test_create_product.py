from decimal import Decimal
from uuid import UUID, uuid4

from src.application.product.commands import CreateProduct, CreateProductHandler
from src.domain.product.value_objects import ProductId, ProductProperty
from tests.mocks import EventMediatorMock, ProductRepoMock, UnitOfWorkMock


async def test_create_product_handler(
    product_repo: ProductRepoMock,
    uow: UnitOfWorkMock,
    event_mediator: EventMediatorMock,
) -> None:
    handler = CreateProductHandler(product_repo, uow)

    product_id: UUID = uuid4()
    command = CreateProduct(
        product_id=product_id, title="Milk", price=Decimal("12.010"), weight=0.5
    )

    product_id_result = await handler(command)

    assert product_id == product_id_result
    product = product_repo.products[ProductId(product_id)]

    assert product.id == ProductId(product_id)
    assert product.product_property == ProductProperty(
        command.title,
        command.price,
        command.weight
    )

    assert uow.commited is True
    assert uow.rolled_back is False
