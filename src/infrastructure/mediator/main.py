from didiator import (
    CommandDispatcherImpl,
    EventObserverImpl,
    Mediator,
    MediatorImpl,
    QueryDispatcherImpl,
)
from didiator.interface.utils.di_builder import DiBuilder
from didiator.middlewares.di import DiMiddleware

from src.application.product.commands import CreateProduct, CreateProductHandler
from src.application.product.queries import GetProducts, GetProductsHandler
from src.infrastructure.di import DiScope


def init_mediator(di_builder: DiBuilder) -> Mediator:
    middlewares = DiMiddleware(di_builder, scopes=DiScope(DiScope.REQUEST))
    command_dispatcher = CommandDispatcherImpl(middlewares=middlewares)
    query_dispatcher = QueryDispatcherImpl(middlewares=middlewares)
    event_observer = EventObserverImpl(middlewares=middlewares)

    mediator = MediatorImpl(
        command_dispatcher, query_dispatcher, event_observer
    )
    return mediator


def setup_mediator(mediator: Mediator) -> None:
    mediator.register_command_handler(CreateProduct, CreateProductHandler)
    mediator.register_query_handler(GetProducts, GetProductsHandler)
