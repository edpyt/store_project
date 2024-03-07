from litestar.dto import DataclassDTO

from src.application.product.commands.create_product import CreateProduct
from src.application.product.dto.products import ProductDTO


class CreateProductDTO(DataclassDTO[CreateProduct]):
    ...


class ReturnProductDTO(DataclassDTO[ProductDTO]):
    ...
