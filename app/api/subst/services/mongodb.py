# db
from pymongo import MongoClient

# dates
import pytz
import datetime
# hash
import json
import hashlib

# types
from typing import List, Union

# env
import os
from dotenv import load_dotenv

load_dotenv()

# helpers

timezone = pytz.timezone(os.environ.get("HOTZ"))


def _date_to_datetime(datum: datetime.date):
    return datetime.datetime.combine(datum, datetime.datetime.min.time(), tzinfo=pytz.UTC)


def _hash(data: list) -> str:
    return hashlib.md5(json.dumps(data).encode('utf-8')).hexdigest()


# algorithms

def _updateSubstitution(col, date_, grade: str, subst: list,) -> Union[None, int]:
    shash = _hash(subst)
    ctime: datetime.datetime = datetime.datetime.utcnow()

    lupdate = list(col.find().sort("_id", -1).limit(1))

    if not lupdate:
        col.insert_one({
            "metas": {
                "ctime": ctime,
                "prev": 0,
                "_": _date_to_datetime(date_),
                "next": 0
            },
            "grade": grade,
            "shash": shash,
            "subst": subst
        })
        return date_

    lupdate = lupdate[0]

    lupdate_shash = lupdate['shash']
    lupdate_metas__ = lupdate['metas']['_'].date()

    if date_ > lupdate_metas__:
        # incomming document is newer then the last inserted one

        col.insert_one({
            "metas": {
                "ctime": ctime,
                "prev": _date_to_datetime(lupdate_metas__),
                "_": _date_to_datetime(date_),
                "next": 0
            },
            "grade": grade,
            "shash": shash,
            "subst": subst
        })

        # update the 'next' field of the preceding document
        col.find_one_and_update(
            filter={'metas._': _date_to_datetime(lupdate_metas__)},
            update={
                '$set': {
                    'metas.next': _date_to_datetime(date_)
                }
            }
        )
        return date_

    elif lupdate_metas__ == date_:
        # incomming document has same date as the last inserted one
        if lupdate_shash == shash:
            return None
        else:
            col.find_one_and_update(
                filter={'metas._': _date_to_datetime(date_)},
                update={
                    '$set': {
                        'metas.ctime': ctime,
                        'shash': shash,
                        'subst': subst
                    }
                }
            )
            return date_
    else:
        # incomming document is older then the last inserted one

        if date_ < datetime.datetime.now(tz=timezone).date():
            return None
        else:
            alupdated = col.find_one(
                filter={
                    'metas._': _date_to_datetime(date_)
                }
            )

            if not alupdated or alupdated['shash'] == shash:
                return None

            else:
                col.find_one_and_update(
                    filter={'metas._': _date_to_datetime(date_)},
                    update={
                        '$set': {
                            'metas.ctime': ctime,
                            'shash': shash,
                            'subst': subst
                        }
                    }
                )
                return date_


def _updateNews(col, date_, news_: list) -> Union[None, int]:
    nhash = _hash(news_)
    ctime = datetime.datetime.utcnow()

    # retrieve the last inserted document

    lupdate = list(col.find().sort("_id", -1).limit(1))

    if not lupdate:
        col.insert_one({
            "metas": {
                "ctime": ctime,
                "prev": 0,
                "_": _date_to_datetime(date_),
                "next": 0
            },
            "nhash": nhash,
            "news_": news_
        })
        return date_

    lupdate = lupdate[0]

    lupdate_nhash = lupdate['nhash']
    lupdate_metas__ = lupdate['metas']['_'].date()

    if date_ > lupdate_metas__:
        # incomming document is newer then the last inserted one

        col.insert_one({
            "metas": {
                "ctime": ctime,
                "prev": _date_to_datetime(lupdate_metas__),
                "_": _date_to_datetime(date_),
                "next": 0
            },
            "nhash": nhash,
            "news_": news_
        })

        # uodate the 'next' field of the preceding document
        col.find_one_and_update(
            filter={'metas._': _date_to_datetime(date_)},
            update={
                '$set': {
                    'metas.next': _date_to_datetime(date_)
                }
            }
        )
        return date_

    elif lupdate_metas__ == date_:
        # incoming document has same creation date as the last inserted one

        if lupdate_nhash == nhash:
            return None

        else:
            col.find_one_and_update(
                filter={'metas._': _date_to_datetime(date_)},
                update={
                    '$set': {
                        'metas.ctime': ctime,
                        'nhash': nhash,
                        'news_': news_
                    }
                }
            )
            return date_
    else:
        # incomming document is older then the last inserted one
        if date_ < datetime.datetime.now(tz=timezone).date():
            return None

        else:
            alupdated = col.find_one(
                filter={
                    'metas._': _date_to_datetime(date_)
                }
            )

            if not alupdated or alupdated['hash'] == nhash:
                return None
            else:
                col.find_one_and_update(
                    filter={'metas._': _date_to_datetime(date_)},
                    update={
                        '$set': {
                            'metas.ctime': ctime,
                            'nhash': nhash,
                            'news_': news_
                        }
                    }
                )
                return date_


class Connector:
    def __init__(self):
        self.client = MongoClient(os.environ.get("MOST"))
        db = self.client.get_database(os.environ.get("DBNA"))
        self.col_test = db.get_collection('test')
        self.col_news = db.get_collection('news')

    # inserters

    def insertUpdateSubstitution(self, date_: datetime.date, subs_: list):
        _updateSubstitution(
            col=self.col_test,
            grade="Q2",
            date_=date_,
            subst=subs_
        )

    def insertUpdateNews(self, date_: datetime.date, news_: List[str]):
        _updateNews(
            col=self.col_news,
            date_=date_,
            news_=news_
        )

    # commons

    @ staticmethod
    def _getByDate(coll, date_: datetime.date, _filters: list[dict[str, str]] = None) -> dict:
        date_ = _date_to_datetime(date_)
        data_ = coll.find_one(filter={'metas._': date_})
        if data_:
            # filtering
            if _filters:
                for block in data_['subst']:
                    for entry in block['entries']:
                        for _filter in _filters:
                            if entry['subject'] != _filter['sid'] and entry['group'] != _filter['gid']:
                                try:
                                    block['entries'].remove(entry)
                                except Exception:
                                    pass

                            if len(block['entries']) == 0:
                                try:
                                    data_['subst'].remove(block)
                                except Exception:
                                    pass

                # return
            return dict(data_)

    @ staticmethod
    def _getLast(coll) -> dict:
        data_ = coll.find().sort("_id", -1).limit(1)
        if data_:
            return dict(list(data_)[0])

    # substitution getters
    def getSubstitution(self, date_: datetime.date, _filters=None):
        return self._getByDate(self.col_test, date_=date_, _filters=_filters)

    def getLastSubstitution(self):
        return self._getLast(self.col_test)

    # news getters
    def getNews(self, date_: datetime.date) -> list:
        data_ = self._getByDate(self.col_news, date_=date_)
        if data_:
            return data_['news_']

    def getLastNews(self) -> list:
        data_ = self._getLast(self.col_news)
        if data_:
            return data_['news_']

    # close
    def close(self):
        self.client.close()
