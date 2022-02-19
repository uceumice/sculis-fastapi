from fastapi import FastAPI
from app.service.api.gateway.base import main as base_gateway

app = FastAPI(
    debug=False,
    title="Sculis API Gateway",
    description="""
*Vertretung, Stundenplan und Kommunikation. Alles in einem API! 🚀*
""",
    version="alpha",
    terms_of_service="/tos#API",
    contact={'Alex': "alexandrutocar@gmail.com"},
    docs_url=False,
    redoc_url=False
)
app.include_router(base_gateway.router, prefix='/api/v2')
