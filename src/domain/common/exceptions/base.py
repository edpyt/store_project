from dataclasses import dataclass


@dataclass(eq=False)
class AppExceptionError(Exception):
    status: int = 500

    @property
    def title(self) -> str:
        return "An app error"
