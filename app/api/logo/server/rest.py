from typing import Optional
from app.api.logo.services.responses import SvgResponse, PngResponse
from app.api.logo.services.image import svg2png_
from app.api.logo.utils.utils import STATIC_DIR


def GET_png_logo(res: Optional[int] = None, _for: Optional[str] = None) -> PngResponse:
    return PngResponse(svg2png_(STATIC_DIR+'/logo.svg', res))

def GET_svg_logo():
    return SvgResponse(STATIC_DIR+'/logo.svg')
