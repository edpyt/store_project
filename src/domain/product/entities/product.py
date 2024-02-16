from dataclasses import dataclass

from src.domain.common.entities.aggregate_root import AggregateRoot


@dataclass
class Product(AggregateRoot):
    ...
