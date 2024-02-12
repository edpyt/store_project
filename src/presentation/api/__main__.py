from src.presentation.api.main import build_app, run_app


async def main() -> None:
    app = build_app()
    await run_app(app)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
