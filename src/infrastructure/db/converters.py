from src.domain.product import entities
from src.infrastructure.db import models


def convert_product_entity_to_db_model(
    product: entities.Product,
) -> models.Product:
    return models.Product(
        id=product.id.to_raw(),
        title=product.product_property.title,
        weight=product.product_property.weight,
        price=product.product_property.price,
    )
