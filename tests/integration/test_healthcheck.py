from litestar.testing.client import AsyncTestClient


async def test_fetch_healtchcheck(test_client: AsyncTestClient) -> None:
    response = await test_client.get("/healthcheck")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
