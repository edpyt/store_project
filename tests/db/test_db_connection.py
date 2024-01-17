import pytest

from sqlalchemy.ext.asyncio.engine import AsyncEngine


@pytest.mark.asyncio
async def test_db_connected(engine: AsyncEngine):
    assert engine  # Should not raise error
