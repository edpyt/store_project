from typing import Generic, Protocol, TypeVar

CRes = TypeVar("CRes", covariant=True)


class Command(Protocol, Generic[CRes]):
    ...


C = TypeVar("C", bound=Command, covariant=True)


class CommandHandler(Protocol, Generic[C, CRes]):
    ...
