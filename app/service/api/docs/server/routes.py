from fastapi import APIRouter

from app.service.api.docs.server.rest import GET_swagger_docs, GET_redoc_docs


router = APIRouter(
    tags=['documentation']
)

# reconfigure swagger documentation page


@router.get("", include_in_schema=False)
async def swagger_docs():
    return GET_swagger_docs()


# reconfigure redoc documentation page
# @router.get("")
# async def redoc_docs():
#     return GET_redoc_docs()
