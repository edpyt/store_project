
from litestar import MediaType, Request, Response


def all_exceptions_handler(_: Request, exc: Exception) -> Response:

    return Response(
        media_type=MediaType.JSON,
        content={"error": "Something went wrong!"},
        status_code=500,
    )
