from src.domain.common.exceptions import AppException


class ApplicationError(AppException):
    @property
    def title(self) -> str:
        return "An application exception"


class RepoError(ApplicationError):
    ...
