from functools import wraps
from typing import Any, Callable, Coroutine, ParamSpec, TypeVar

from sqlalchemy.exc import SQLAlchemyError

from src.application.common.exceptions import RepoError

Param = ParamSpec("Param")
ReturnType = TypeVar("ReturnType")



def exception_mapper(
    func: Callable[Param, Coroutine[Any, Any, ReturnType]],
) -> Callable[Param, Coroutine[Any, Any, ReturnType]]:
    @wraps
    async def wrapped(*args: Param.args, **kwargs: Param.kwargs) -> ReturnType:
        try:
            return await func(*args, **kwargs)
        except SQLAlchemyError as err:
            raise RepoError from err
    return wrapped  # type: ignore
