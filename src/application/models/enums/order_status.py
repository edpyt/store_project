from enum import auto, StrEnum


class Status(StrEnum):
    CREATED = auto()
    IN_DELIVERY = auto()
    DELIVERED = auto()
