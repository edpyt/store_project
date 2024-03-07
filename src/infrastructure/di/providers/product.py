from dishka import Provider, Scope, provide

from src.application.product.commands.create_product import (
    CreateProductHandler,
)
from src.application.product.interfaces.persistence.reader import ProductReader
from src.application.product.interfaces.persistence.repo import ProductRepo
from src.infrastructure.db.repositories.product import (
    ProductReaderImpl,
    ProductRepoImpl,
)


class ProductProvider(Provider):
    product_repo = provide(
        ProductRepoImpl, scope=Scope.REQUEST, provides=ProductRepo
    )
    product_reader = provide(
        ProductReaderImpl, scope=Scope.REQUEST, provides=ProductReader
    )
    create_product_handler = provide(CreateProductHandler, scope=Scope.REQUEST)
