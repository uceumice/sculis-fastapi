from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.security import http
from fastapi.staticfiles import StaticFiles

FAVICON_PATH = "static/favicon_io/favicon.ico"

app = FastAPI(docs_url=None)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/docs", include_in_schema=False)
async def swagger_ui_html():
    # rewrites the default docs to include the right favicon.ico
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="FastAPI",
        swagger_favicon_url=FAVICON_PATH
    )


@app.get("/favicon.ico", include_in_schema=False)
async def get_favicon():
    # sets the url for the favicon.ico
    return FileResponse(FAVICON_PATH)


@app.get("/")
async def read_root():
    return {"ding": "dong"}
