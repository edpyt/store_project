from litestar import MediaType, Request, Response


def all_exceptions_handler(_: Request, exc: Exception) -> Response:
    # TODO: add logger
    print(exc)  # noqa
    return Response(
        media_type=MediaType.JSON,
        content={"error": "Something went wrong!"},
        status_code=500,
    )
