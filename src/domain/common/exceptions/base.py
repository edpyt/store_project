from dataclasses import dataclass
from typing import ClassVar


@dataclass(eq=False)
class AppException(Exception):
    status: ClassVar[int] = 500

    @property
    def title(self) -> str:
        return "An app error"


class DomainException(AppException):
    @property
    def title(self) -> str:
        return "A domain error"
