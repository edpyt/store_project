from litestar import Response, get


@get(
    "/healthcheck",
    status_code=200,
    summary="GET health service",
    tags=["Healtcheck"],
)
def healthcheck_endpoint() -> Response:
    return Response({"status": "ok"}, status_code=200)
