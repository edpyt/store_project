import os


def run_cli() -> None:
    os.environ.setdefault("LITESTAR_APP", "src.presentation.api.main:init_api")
    os.environ["LITESTAR_WARN_IMPLICIT_SYNC_TO_THREAD"] = "0"
    from litestar.__main__ import run_cli as run_litestar_cli

    run_litestar_cli()


if __name__ == "__main__":
    run_cli()
