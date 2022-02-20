from fastapi import APIRouter, Query

from app.service.api.logo.utils.utils import STATIC_DIR
from app.service.api.logo.server.rest import GET_png_logo, GET_svg_logo


router = APIRouter(tags=['Logo'])


# logo.png
@router.get("/logo.png", include_in_schema=True)
async def png_logo(res: int = Query(1000, gt=0, le=3000), _for: str = Query(None, alias='for')):
    # sets the url for the favicon.ico
    return GET_png_logo(res, _for)


# logo.svg
@router.get("/logo.svg", include_in_schema=True)
async def svg_logo():
    # sets the url for the favicon.ico
    return GET_svg_logo()
