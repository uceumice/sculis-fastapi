from fastapi import APIRouter
from app.api.logo.server import routes as logo
from app.api.subst.server import routes as subst

router = APIRouter()


router.include_router(logo.router, prefix="/logo")
router.include_router(subst.router, prefix='/s')

