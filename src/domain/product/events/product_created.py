from dataclasses import dataclass
from decimal import Decimal
from uuid import UUID

from src.domain.common.events.event import Event


@dataclass(frozen=True)
class ProductCreated(Event):
    product_id: UUID
    title: str
    weight: float
    price: Decimal
