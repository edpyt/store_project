from dataclasses import dataclass

from src.application.common.dto import DTO


@dataclass
class Product(DTO):
    title: str
