from fastapi import APIRouter
from app.service.api.logo.server import routes as logo

router = APIRouter()
# must always be static
router.include_router(logo.router, prefix="/logo")
# router.include_router(some_other_microservice, '/some_other_microservice')
