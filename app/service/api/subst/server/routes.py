from fastapi import APIRouter, Path, Query

from app.service.api.logo.utils.utils import STATIC_DIR
from app.service.api.logo.server.rest import GET_png_logo, GET_svg_logo


router = APIRouter(tags=['Substitution'])


@router.get("/subst/{date}", include_in_schema=True)
async def subst(
    date: str = Path(regex=r"^\d{4}-([0]\d|1[0-2])-(0[1-9]|[1-2]\d|3[01])$"),
    o: dict = Query(default=None)
):  
    return None


@router.get("/news", include_in_schema=True)
async def news(o: dict = Query(default=None)):
    return None
