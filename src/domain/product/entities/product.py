from dataclasses import dataclass, field
from typing import Self

from src.domain.common.entities.aggregate_root import AggregateRoot
from src.domain.product.events.product_created import ProductCreated
from src.domain.product.exceptions import ProductPropertyAlreadyExists
from src.domain.product.value_objects import ProductId, ProductProperty


@dataclass
class Product(AggregateRoot):
    id: ProductId
    product_property: ProductProperty
    existing_product_properties: set[ProductProperty] = field(
        default_factory=set
    )

    @classmethod
    def create(
        cls,
        product_id: ProductId,
        product_property: ProductProperty,
        existing_product_properties: set[ProductProperty],
    ) -> Self:
        if product_property in existing_product_properties:
            raise ProductPropertyAlreadyExists(product_property.to_raw())

        existing_product_properties.add(product_property)
        product = cls(product_id, product_property, existing_product_properties)
        product.record_event(
            ProductCreated(
                product_id.to_raw(),
                *product_property.to_raw(),
            )
        )
        return product
