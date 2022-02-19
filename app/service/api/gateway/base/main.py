from fastapi import APIRouter
from app.service.api.static.server import routes as static
from app.service.api.docs.server import routes as docs

router = APIRouter()
router.include_router(router=static.router, prefix="/static") # must always be static
router.include_router(router=docs.router, prefix="/docs")
