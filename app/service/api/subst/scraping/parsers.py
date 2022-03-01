from typing import Tuple

GRADES = {
    'Q2': ["Q2", "q2"]
}


def parseStatus(anmerkung, raumwechsel):
    status: str

    if raumwechsel:
        status = 'raumwechsel'
    elif "EVA" in anmerkung:
        status = 'eva'
    elif "Teams" in anmerkung:
        status = 'teams'
    elif "" == anmerkung:
        status = 'ausfall'
    else:
        status = 'divers'

    return status


def parseGrade(text: str) -> Tuple:
    # strip spaces
    stufe = text.replace(" ", "")

    for stufe_name, moegliche_namen in GRADES.items():
        if stufe in moegliche_namen:
            return stufe_name


def parseSubjectGroup(text: str) -> Tuple:
    fachkurs = text.split()

    if len(fachkurs) == 1:
        fach = fachkurs[0]
        kurs = None
    elif len(fachkurs) == 2:
        fach, kurs = fachkurs
    else:
        fach = " ".join(fachkurs)
        kurs = None

    return fach, kurs


def parseClass_(text: str) -> Tuple[int]:
    # strip spaces
    text = text.replace(" ", "")

    # range (von, bis) Stunde
    if "-" in text:
        von, bis = [int(i) for i in text.split("-")]
    else:
        von, bis = [int(i) for i in [text]*2]
    return von, bis


def parseRoomRoomChange(text: str) -> Tuple[str]:
    # TODO finde Beispiele und implementiere
    # entsprechenden Parser
    return text, None


def parseNotice(text: str) -> str:
    if text == "\xa0":
        return ""
    return text
