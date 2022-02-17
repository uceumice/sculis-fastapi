import os
from fastapi import Depends, FastAPI, Response, Security, status
from fastapi.responses import FileResponse, JSONResponse
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html
from fastapi.staticfiles import StaticFiles
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from ....utils.utils import VerifyToken

STATIC_PATH = 'app/static'


def staticfile(srel_path: os.PathLike):
    return os.path.join(STATIC_PATH+srel_path)


token_auth_scheme = HTTPBearer()

# create an APP instance
app = FastAPI(
    title="SCULIS Gateway API",
    docs_url=None,
    redoc_url=None
)
# add static files root
app.mount("/static", StaticFiles(directory=STATIC_PATH), name="static")


# reconfigure swagger documentation page
@app.get("/docs", include_in_schema=False)
async def swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="SCULIS API Docs",
        swagger_favicon_url=staticfile('/favicon_io/favicon.ico')
    )


# reconfigure redoc documentation page
@app.get("/redoc", include_in_schema=False)
async def redoc_ui_html():
    return get_redoc_html(
        openapi_url="/openapi.json",
        title="SCULIS API Docs",
        swagger_favicon_url=staticfile('/favicon_io/favicon.ico')
    )


# favicon.ico
@app.get("/favicon.ico", include_in_schema=False)
async def get_favicon():
    # sets the url for the favicon.ico
    return FileResponse(staticfile('/favicon_io/favicon.ico'))


# logo.png
@app.get("/logo.png", include_in_schema=False)
async def get_favicon():
    # sets the url for the favicon.ico
    return FileResponse(staticfile('/favicon_io/logo-512x512.png'))


# ########################################################################################################################################


@app.get("/")
async def read_root():
    return {"ding": "dong"}


@app.get('/private')
async def get_private_route(response: Response, token: HTTPAuthorizationCredentials = Depends(token_auth_scheme)):
    result = VerifyToken(token.credentials).verify()

    if result.get('status'):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return result

    return result


@app.get('/private_scopes')
async def get_private_access_route(token: str = Security(token_auth_scheme, scopes={'private:access'})):
    return JSONResponse({'private ding': 'private dong'})
