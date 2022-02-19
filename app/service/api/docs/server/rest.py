import os
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html
from fastapi.responses import HTMLResponse, JSONResponse


COMMON = {
    "openapi_url": "/openapi.json",
    "title": "Sculis API Docs",
}

SWAGGER_FAVICON_URL = REDOC_FAVICON_URL = "/static/favicon.ico"


def GET_swagger_docs() -> HTMLResponse:
    return get_swagger_ui_html(**COMMON, swagger_favicon_url=SWAGGER_FAVICON_URL, )


def GET_redoc_docs() -> HTMLResponse:
    return get_redoc_html(**COMMON, redoc_favicon_url=REDOC_FAVICON_URL)
