from fastapi import APIRouter, Path, Query

from app.service.api.subst.server.rest import GET_subst, GET_news


router = APIRouter(tags=['Substitution'])


@router.get("/test/subst/{date}", include_in_schema=True)
async def subst(date: str = Path(..., regex=r"^\d{4}-([0]\d|1[0-2])-(0[1-9]|[1-2]\d|3[01])$"), o: str = Query(default=None)):
    return GET_subst(dstr=date, o=o)


@router.get("/test/news/{date}", include_in_schema=True)
async def list_news(date: str = Path(..., regex=r"^\d{4}-([0]\d|1[0-2])-(0[1-9]|[1-2]\d|3[01])$")):
    return GET_news(dstr=date)
