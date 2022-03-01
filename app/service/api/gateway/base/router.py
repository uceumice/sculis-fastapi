from fastapi import APIRouter
from app.service.api.logo.server import routes as logo
from app.service.api.subst.server import routes as subst

router = APIRouter()


router.include_router(logo.router, prefix="/logo")
router.include_router(subst.router, prefix='/s')

