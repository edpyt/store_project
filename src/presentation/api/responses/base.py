from typing import Any

from litestar import Response
from litestar.background_tasks import BackgroundTask, BackgroundTasks
from litestar.enums import MediaType, OpenAPIMediaType
from litestar.types import ResponseCookies, ResponseHeaders, TypeEncodersMap


class OkResponse(Response):
    def __init__(
        self,
        content: Any,
        *,
        background: BackgroundTask | BackgroundTasks | None = None,
        cookies: "ResponseCookies | None" = None,
        encoding: str = "utf-8",
        headers: "ResponseHeaders | None" = None,
        media_type: "MediaType | OpenAPIMediaType | str | None" = None,
        status_code: int | None = None,
        type_encoders: "TypeEncodersMap | None" = None,
    ) -> None:
        assert status_code in range(
            200, 300
        ), "You're using `OkResponse`. Must be valid 2** status code"
        super().__init__(
            content,
            background=background,
            cookies=cookies,
            encoding=encoding,
            headers=headers,
            media_type=media_type,
            status_code=status_code,
            type_encoders=type_encoders,
        )
