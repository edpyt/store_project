from src.domain.common.exceptions import AppException


class ApplicationError(AppException):
    @property
    def title(self) -> str:
        return "An application exception"


class UnexpectedError(ApplicationError):
    ...


class RepoError(ApplicationError):
    ...


class CommitError(UnexpectedError):
    ...


class RollbackError(UnexpectedError):
    ...
