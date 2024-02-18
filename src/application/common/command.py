from typing import Generic, Protocol, TypeVar

CRes = TypeVar("CRes")


class Command(Protocol, Generic[CRes]):
    ...


C = TypeVar("C", bound=Command)


class CommandHandler(Protocol, Generic[C, CRes]):
    ...
