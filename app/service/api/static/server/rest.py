from typing import Optional
from app.service.api.static.services.responses import SvgResponse, PngResponse, IcoResponse
from app.service.api.static.services.image import logo
from app.service.api.static.utils.utils import STATIC_DIR
import os


def GET_favicon():
    with open(STATIC_DIR+"/favicon.ico", 'rb') as f:
        return IcoResponse(f)


def GET_png_logo(res: Optional[int] = None, _for: Optional[str] = None) -> PngResponse:
    if not any({res, _for}):
        return ValueError('Either res or _for argument must be specified')
    if res == 512 or _for == "android-chrome-512x512":
        return GET_android_chrome_icon_512x512()
    elif res == 192 or _for == "android-chrome-192x192":
        return GET_android_chrome_icon_192x192()
    elif res == 180 or _for == "apple-touch-icon":
        return GET_apple_touch_icon()
    elif res == 32 or _for == "favicon-32x32":
        return GET_favicon_32x32()
    elif res == 16 or _for == "favicon-16x16":
        return GET_favicon_16x16()
    else:
        return PngResponse(logo(STATIC_DIR+'/logos/logo.svg', res))


def GET_svg_logo():
    return SvgResponse(STATIC_DIR+'/logos/logo.svg')


# UNUSED


def GET_apple_touch_icon():
    return PngResponse(STATIC_DIR+"/logos/apple-touch-icon.png")


def GET_android_chrome_icon_192x192():
    return PngResponse(STATIC_DIR+"/logos/android-chrome-192x192.png")


def GET_android_chrome_icon_512x512():
    return PngResponse(STATIC_DIR+"/logos/android-chrome-512x512.png")


def GET_favicon_16x16():
    return PngResponse(STATIC_DIR+"/logos/favicon-16x16.png")


def GET_favicon_32x32():
    return PngResponse(STATIC_DIR+"/logos/favicon-32x32.png")
