from dataclasses import dataclass

from src.domain.common.value_objects.base import ValueObject


@dataclass(frozen=True)
class Title(ValueObject[str | None]):
    value: str | None

    def _validate(self) -> None:
        ...
