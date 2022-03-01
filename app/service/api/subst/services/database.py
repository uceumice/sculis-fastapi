from datetime import date
from pymongo import MongoClient
import os

client = MongoClient(os.getenv("MONGOCS"))

db = client[os.getenv("MONGODN")]
cl = db[os.getenv("MONGOCN")]

def _fake_dt(_date: date):
    return date


def get_dates():
    return None

def get_subst(_date: date, filters: dict[str, str]):
    cl.find_one(
        filter={'meta.aktuell': _date}
    )
