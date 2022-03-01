from datetime import datetime
from typing import Optional
from app.service.api.logo.services.responses import SvgResponse, PngResponse
from app.service.api.logo.services.image import logo
from app.service.api.logo.utils.utils import STATIC_DIR


def GET_subst(dstr: str, o: dict = None) -> dict:
    date = datetime.strptime(dstr, "%Y-%m-%d").date()
    
    return date