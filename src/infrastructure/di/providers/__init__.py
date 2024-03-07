from dataclasses import astuple, dataclass
from typing import Iterable

from .db import DBProvider
from .event_bus import EventBusProvider
from .main import MainProvider
from .product import ProductProvider

__all__ = ("DBProvider", "EventBusProvider", "MainProvider", "ProductProvider")


@dataclass(frozen=True)
class DiProviders:
    main: MainProvider
    db: DBProvider
    product: ProductProvider

    def __iter__(self) -> Iterable:
        return iter(astuple(self))
