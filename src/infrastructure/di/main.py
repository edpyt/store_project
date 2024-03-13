from src.infrastructure.di.providers import (
    DBProvider,
    DiProviders,
    MainProvider,
    MessageBrokerProvider,
    ProductProvider,
    UOWProvider,
)


def setup_providers() -> DiProviders:
    di_providers = DiProviders(
        main=MainProvider(),
        db=DBProvider(),
        product=ProductProvider(),
        uow=UOWProvider(),
        message_broker=MessageBrokerProvider(),
    )
    return di_providers
