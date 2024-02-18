from dataclasses import dataclass
from uuid import UUID

from src.domain.common.value_objects.base import ValueObject


@dataclass(frozen=True)
class ProductId(ValueObject[UUID]):
    value: UUID
