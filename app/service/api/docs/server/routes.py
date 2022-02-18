from fastapi import APIRouter

from app.service.api.docs.server.rest import GET_swagger_docs, GET_redoc_docs


router = APIRouter()


# reconfigure swagger documentation page
@router.get("/swagger")
async def swagger_ui_html():
    return GET_swagger_docs()


# reconfigure redoc documentation page
@router.get("/redoc")
async def redoc_ui_html():
    return GET_redoc_docs()
