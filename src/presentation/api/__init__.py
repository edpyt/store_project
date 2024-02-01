from fastapi import APIRouter


def setup() -> APIRouter:
    router = APIRouter()
    router.include_router()
