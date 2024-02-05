from dataclasses import dataclass
from decimal import Decimal

from src.application.common.dto import DTO


@dataclass
class ProductDTO(DTO):
    title: str
    price: Decimal
    weight: float