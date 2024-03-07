from src.infrastructure.di.providers import (
    DBProvider,
    DiProviders,
    MainProvider,
    ProductProvider,
)


def setup_providers() -> DiProviders:
    main_provider = MainProvider()
    db_provider = DBProvider()
    product_provider = ProductProvider()

    di_providers = DiProviders(
        main=main_provider, db=db_provider, product=product_provider
    )
    return di_providers
