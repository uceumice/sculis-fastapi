# exceptions
from fastapi.exceptions import HTTPException

# dates
from datetime import datetime

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
