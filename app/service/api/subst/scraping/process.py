import json
import logging
import sys
import time
import os

from app.service.api.subst.services.mongodb import Connector
from scraper import SubstitutionScraper

SCRIPTDIR = os.path.dirname(os.path.abspath(__file__))

def config_logger():
    logger = logging.getLogger("test")
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '%(name)s | %(asctime)s | %(message)s'
    )

    # log in file
    fh = logging.FileHandler(f"{SCRIPTDIR}/debug.log")
    fh.setLevel(logging.ERROR)
    fh.setFormatter(formatter)

    # log in terminal
    fs = logging.StreamHandler(sys.stdout)
    fs.setLevel(logging.DEBUG)
    fs.setFormatter(formatter)

    logger.addHandler(fs)
    logger.addHandler(fh)

    return logger

logger = config_logger()


def config_intervaal(tag: int = 0, stunde: int = 0, minute: int = 0, sekunde: int = 0):
    return sekunde + 60*minute + stunde*60*60 + tag*24*60*60


INTERVAAL = config_intervaal(minute=2)


def update():
    # establish connection to the database
    connector = Connector()
    
    # collect links to retrieve data from
    for link in json.loads(os.environ.get("LINKS")):
        # instantiate scraper
        scraper = SubstitutionScraper(link)

        # parse site date
        date_ = scraper.getDate()

        # update substitution
        connector.insertUpdateSubstitution(date_=date_, subs_=scraper.getSubstitution())

        # update news
        connector.insertUpdateNews( date_=date_, news_=scraper.getNews())
    
    connector.close()


logger.debug("'%s' started." % (__file__))

while True:
    try:
        start = time.time()
        update()
        end = time.time()
        logger.debug(f"Updated in {end - start} sec")
    except Exception as e:
        logger.error(e)
    logger.debug(f"Wait {INTERVAAL} sec")
    time.sleep(INTERVAAL)

