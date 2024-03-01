import asyncio

import pytest


@pytest.fixture(scope="session")
def event_loop():
    """Creates an instance of the default event loop for the test session."""
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()

    try:
        yield loop
    finally:
        loop.close()
