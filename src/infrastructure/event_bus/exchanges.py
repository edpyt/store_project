from src.infrastructure.message_broker import MessageBroker


async def declare_exchanges(message_broker: MessageBroker) -> None:
    await message_broker.declare_exchange("product")
