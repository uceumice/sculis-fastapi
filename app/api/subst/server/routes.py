from fastapi import APIRouter, Path, Query

from app.api.subst.server.rest import GET_subst, GET_news, GET_dates, GET_closest_date


router = APIRouter(tags=['Substitution'])


@router.get("/test/subst/{date}", include_in_schema=True)
async def subst(date: str = Path(..., regex=r"^\d{4}-([0]\d|1[0-2])-(0[1-9]|[1-2]\d|3[01])$"), o: str = Query(default=None)):
    return GET_subst(dstr=date, o=o)


@router.get("/test/news/{date}", include_in_schema=True)
async def news(date: str = Path(..., regex=r"^\d{4}-([0]\d|1[0-2])-(0[1-9]|[1-2]\d|3[01])$")):
    return GET_news(dstr=date)


@router.get("/test/dates", include_in_schema=True)
async def dates():
    return GET_dates()


@router.get("/test/date", include_in_schema=True)
async def dates():
    return GET_closest_date()
