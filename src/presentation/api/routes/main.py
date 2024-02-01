from fastapi import FastAPI


def setup_controllers(app: FastAPI) -> None:
    app.add_api_route()
