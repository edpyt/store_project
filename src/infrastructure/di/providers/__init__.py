from dataclasses import astuple, dataclass
from typing import Iterable

from .db import DBProvider
from .main import MainProvider
from .message_broker import MessageBrokerProvider
from .product import ProductProvider
from .uow import UOWProvider

__all__ = ("DBProvider", "MessageBrokerProvider", "MainProvider", "ProductProvider")


@dataclass(frozen=True)
class DiProviders:
    db: DBProvider | None = None
    main: MainProvider | None = None
    uow: UOWProvider | None = None
    message_broker: MessageBrokerProvider | None = None
    product: ProductProvider | None = None

    def __iter__(self) -> Iterable:
        return filter(None, astuple(self))
