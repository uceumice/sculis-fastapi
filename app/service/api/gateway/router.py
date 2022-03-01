from fastapi import APIRouter
from app.service.api.gateway.base import router as base_gateway

router = APIRouter()

router.include_router(base_gateway.router, prefix="/base")