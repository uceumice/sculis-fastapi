# exceptions
from fastapi.exceptions import HTTPException

# dates
from datetime import date, datetime, timedelta

# subs
from app.utils.mongodb.mongodb import Connector


# url decode & parse
from urllib.parse import unquote
import json

db = Connector()


def GET_subst(dstr: str, o: str = None) -> dict:
    date = datetime.strptime(dstr, "%Y-%m-%d").date()
    if o:
        data_ = db.getSubstitution(date, _filters=json.loads(unquote(o)))
    else:
        data_ = db.getSubstitution(date, None)

    if not data_:
        raise HTTPException(404)

    return data_


def GET_news(dstr: str) -> list:
    date = datetime.strptime(dstr, "%Y-%m-%d").date()
    data_ = db.getNews(date)

    if not data_:
        raise HTTPException(404)

    return data_


def GET_dates() -> list:
    data_ = db.getDates()

    if not data_:
        raise HTTPException(404)

    return data_


def GET_closest_date() -> date:
    dates_ = GET_dates()
    today = datetime.now()

    temp_diff = timedelta()
    temp_date = dates_[0]
    for date_ in dates_[1:]:
        diff_ = today - date_
        if temp_diff:
            if diff_ < temp_diff:
                temp_diff = diff_
                temp_date = date_

    if not temp_date:
        raise HTTPException(404)

    return temp_date
