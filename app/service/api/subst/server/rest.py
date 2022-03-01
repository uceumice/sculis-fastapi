# exceptions
from fastapi.exceptions import HTTPException

# dates
from datetime import datetime

# types
from bson.objectid import ObjectId

# subs
from app.service.api.subst.services.mongodb import Connector


# url decode & parse
from urllib.parse import unquote
import json

db = Connector()


def bson_json_helper(d: dict) -> dict:
    # check if there is any value
    if not d:
        return None

    dl = dict()

    for key, value in d.items():
        if isinstance(value, ObjectId):
            dl[key] = str(value)
        else:
            dl[key] = value
    return dl


def GET_subst(dstr: str, o: str = None) -> dict:
    date = datetime.strptime(dstr, "%Y-%m-%d").date()
    if o:
        data_ = bson_json_helper(db.getSubstitution(date, _filters=json.loads(unquote(o))))
    else:
        data_ = bson_json_helper(db.getSubstitution(date, None))

    if not data_:
        raise HTTPException(404)

    return data_


def GET_news(dstr: str) -> list:
    date = datetime.strptime(dstr, "%Y-%m-%d").date()
    data_ = db.getNews(date)

    if not data_:
        raise HTTPException(404)

    return data_
