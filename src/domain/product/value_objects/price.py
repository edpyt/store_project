from dataclasses import dataclass
from decimal import Decimal

from src.domain.common.value_objects.base import ValueObject


@dataclass(frozen=True)
class Price(ValueObject[Decimal | None]):
    value: Decimal | None

    def _validate(self) -> None:
        ...
