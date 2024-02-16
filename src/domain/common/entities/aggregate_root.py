from dataclasses import dataclass
from typing import Protocol

from .entity import Entity


@dataclass
class AggregateRoot(Entity, Protocol):
    ...
