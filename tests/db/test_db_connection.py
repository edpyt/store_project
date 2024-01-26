import pytest
from sqlalchemy import text

from sqlalchemy.ext.asyncio.session import AsyncSession


@pytest.mark.asyncio()
async def test_db_connected(session: AsyncSession) -> None:
    await session.execute(text("SELECT 1"))
