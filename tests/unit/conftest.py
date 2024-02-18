import pytest

from tests.mocks import EventMediatorMock, ProductRepoMock, UnitOfWorkMock


@pytest.fixture
def product_repo() -> ProductRepoMock:
    return ProductRepoMock()


@pytest.fixture
def event_mediator() -> EventMediatorMock:
    return EventMediatorMock()


@pytest.fixture
def uow() -> UnitOfWorkMock:
    return UnitOfWorkMock()
