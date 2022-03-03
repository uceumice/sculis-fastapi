from fastapi import APIRouter, Query

from app.api.logo.utils.utils import STATIC_DIR
from app.api.logo.server.rest import GET_png_logo, GET_svg_logo


router = APIRouter(tags=['Logo'])


@router.get("/png", include_in_schema=True)
async def png_logo(res: int = Query(1000, gt=0, le=3000), _for: str = Query(None, alias='for')):
    return GET_png_logo(res, _for)


@router.get("/svg", include_in_schema=True)
async def svg_logo():
    return GET_svg_logo()
