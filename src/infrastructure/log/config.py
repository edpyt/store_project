from dataclasses import dataclass
from pathlib import Path


@dataclass
class LoggingConfig:
    path: Path | None = None
    level: str = "DEBUG"
