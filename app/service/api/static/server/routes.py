from fastapi import APIRouter, FastAPI, Query
from fastapi.staticfiles import StaticFiles

from app.service.api.static.utils.utils import STATIC_DIR
from app.service.api.static.server.rest import GET_png_logo, GET_favicon, GET_svg_logo


router = APIRouter(tags=['static files'])
router.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


# favicon.ico
@router.get("/favicon.ico", include_in_schema=False)
async def favicon():
    # sets the url for the favicon.ico
    return GET_favicon()


# logo.png
@router.get("/logo.png", include_in_schema=False)
async def png_logo(res: int = Query(1000, gt=0, le=3000), _for: str = Query(None, alias='for')):
    # sets the url for the favicon.ico
    return GET_png_logo(res, _for)


# logo.svg
@router.get("/logo.svg", include_in_schema=False)
async def svg_logo():
    # sets the url for the favicon.ico
    return GET_svg_logo()
