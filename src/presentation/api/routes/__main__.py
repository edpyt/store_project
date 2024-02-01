from fastapi import APIRouter


def setup() -> APIRouter:
    router = APIRouter()
    router.add_api_route()
