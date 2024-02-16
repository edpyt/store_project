from dataclasses import dataclass

from src.domain.common.value_objects.base import ValueObject


@dataclass(frozen=True)
class Weight(ValueObject[float | None]):
    value: float | None

    def _validate(self) -> None:
        ...
