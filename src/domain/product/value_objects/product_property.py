import re
from dataclasses import dataclass
from decimal import Decimal

from src.domain.common.exceptions.base import DomainException
from src.domain.common.value_objects.base import BaseValueObject

MAX_TITLE_LENGTH = 120
PRODUCT_PATTERN = r"[A-Za-z\s]+"


@dataclass(eq=False)
class WrongTitleValueError(ValueError, DomainException):
    product_title: str
    text: str

    @property
    def title(self) -> str:
        return self.text


class EmptyTitle(WrongTitleValueError):
    ...


class TooLongTitle(WrongTitleValueError):
    ...


class WrongTitleFormat(WrongTitleValueError):
    ...


@dataclass(eq=False)
class PositiveNumericValueError(ValueError, DomainException):
    number: Decimal | float
    text: str

    @property
    def title(self) -> str:
        return str(self.number)


class NegativePrice(PositiveNumericValueError):
    ...


class NegativeWeight(PositiveNumericValueError):
    ...


@dataclass(frozen=True)
class ProductProperty(BaseValueObject):
    title: str
    price: Decimal
    weight: float

    def _validate(self) -> None:
        if len(self.title) == 0:
            raise EmptyTitle(self.title, "Product title can't be empty")
        if len(self.title) > MAX_TITLE_LENGTH:
            raise TooLongTitle(
                self.title, f'Too long product title "{self.title}"'
            )
        if re.match(PRODUCT_PATTERN, self.title) is None:
            raise WrongTitleFormat(
                self.title, f"Wrong title format {self.title}"
            )

        if self.price <= 0:
            raise NegativePrice(self.price, "Price can't be lower or equal zero")
        if self.weight <= 0:
            raise NegativeWeight(self.weight, "Weight can't be lower or equal zero")

    def __str__(self) -> str:
        return f"{self.title} {self.weight} {self.price}"

    def to_raw(self) -> tuple[str, float, Decimal]:
        return self.title, self.weight, self.price
