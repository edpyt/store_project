from enum import StrEnum, auto


class Status(StrEnum):
    CREATED = auto()
    IN_DELIVERY = auto()
    DELIVERED = auto()
