# types
from typing import Dict, List, Union
import datetime

# web
import requests
from bs4 import BeautifulSoup

# subs
from parsers import (
    parseClass_,
    parseGrade,
    parseSubjectGroup,
    parseStatus,
    parseRoomRoomChange,
    parseNotice
)


class SubstitutionScraper:
    def __init__(self, url, **kwargs):
        site = requests.get(url)
        self.soup = BeautifulSoup(site.content, features="html.parser")
        self.test = []
        self.news = []

        self.scrapDate()
        self.scrapSubstitution()
        self.scrapNews()

    # getters

    def getDate(self):
        return self.date

    def getSubstitution(self):
        return self.test

    def getNews(self) -> List[str]:
        return self.news

    # scrapers

    def scrapDate(self) -> datetime.date:
        # yields 31.12.2020 Montag
        date_ = self.soup.find('div', {'class': 'mon_title'}).text
        # yields 31.12.2020
        date_ = date_.split()[0]
        
        # fast strptime
        date_ = [int(i) for i in date_.split('.')]

        date_ = datetime.date(year=date_[2], month=date_[1], day=date_[0])
        self.date = date_

    def scrapNews(self) -> List[str]:
        # get tabelle spalten <td>
        columns = self.soup.findAll('td', {'class': 'info'})

        # there must be no infomation if
        # there is not a single column
        if columns is None:
            return []

        # using a dict to be able to append to the same key
        news: Dict[int, str] = {}

        # parsing mechanism
        for column in columns:
            # separate each row in a column
            rows: str = column.stripped_strings
            for rowi, row in enumerate(rows):
                # create an empty (placeolder) message
                # to append more to it
                if rowi not in news.keys():
                    news[rowi] = ""
                news[rowi] += " " + row

        self.news = list(news.values())

    def scrapSubstitution(self) -> Dict[int, Dict[int, List[Dict[str, str]]]]:
        # contains the whole vertreutng - table
        table = self.soup.find('table', {'class': 'mon_list'})

        # list of rows in the table, but the column names (1st row)
        rows = table.findAll('tr')[1:]

        # TODO multi-process
        def forEachRow(row):
            cells: List[str] = row.findAll('td')

            # stufe
            grade = parseGrade(cells[0].text)

            # class_ (eine oder mehrere)
            class__from, class__to = parseClass_(cells[1].text)

            # subject und group
            subject, group = parseSubjectGroup(cells[2].text)

            # room und eventuell roomchange
            room, roomchange = parseRoomRoomChange(cells[3].text)

            # notice
            notice = parseNotice(cells[4].text)

            # status und status farbe
            status = parseStatus(notice, roomchange)

            # rules for inserting a standin entry class_ -> Entry
            def insertSubstitutionInList(class_: int, substitutionlist: list):

                def classIndex() -> Union[None, str]:
                    # gibt index für welchen die gerade betrachtete
                    # class_ bereits in der Vertretungsliste gibt
                    if len(substitutionlist) == 0:
                        return -1

                    for stunde_index, vertretung in enumerate(substitutionlist):
                        if vertretung["class_"] == class_:
                            return stunde_index

                    return -1

                def entry() -> dict:
                    return {
                        "status":       status,
                        "subject":         subject,
                        "group":         group,
                        "room":         room,
                        "roomchange":  roomchange,
                        "notice":    notice,
                    }

                class_index = classIndex()

                if class_index == -1:
                    # der eintrag für diese class_ ist neu

                    # uhrzeit_begin, uhrzeit_ende = parseStundeUhrzeiten(class_)

                    substitutionlist.append(
                        {
                            "class_":    class_,
                            "entries": [
                                entry()
                            ]
                        }
                    )
                else:
                    # gleiche class_ gibt es bereits in der Verrtetungsliste
                    substitutionlist[class_index]["entries"].append(
                        entry()
                    )

            def insertEntriesInSubstList(substitutionlist_: list):
                if class__from == class__to:
                    insertSubstitutionInList(class__from, substitutionlist_)
                elif class__from < class__to:
                    class_es = set(range(class__from, class__to+1))
                    for class_ in class_es:
                        insertSubstitutionInList(class_, substitutionlist_)

            if grade == "Q2":
                insertEntriesInSubstList(self.test)

        for row in rows:
            forEachRow(row)
