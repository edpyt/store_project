from src.domain.common.exceptions import AppExceptionError


class ApplicationError(AppExceptionError):
    @property
    def title(self) -> str:
        return "An application exception"
