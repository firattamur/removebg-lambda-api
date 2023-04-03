from fastapi import APIRouter

from .endpoints.removebg import router as removebg_router

router = APIRouter()

router.include_router(removebg_router, prefix="/removebg", tags=["removebg"])
