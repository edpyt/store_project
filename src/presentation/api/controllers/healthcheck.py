from litestar import Response, get


@get(
    "/healthcheck",
    status_code=200,
    summary="GET health service",
    tags=["Healthcheck"],
)
async def healthcheck_endpoint() -> Response:
    return Response({"status": "ok"}, status_code=200)
