from fastapi import FastAPI
from app.service.api.gateway import router as gateway

app = FastAPI(
    debug=True,
    title="Sculis API Gateway",
    description="""
*Vertretung, Stundenplan und Kommunikation. Alles in einem API! 🚀*
""",
    version="alpha",
    terms_of_service="/tos#API",
    contact={'Alex': "alexandrutocar@gmail.com"},
    docs_url=False
)


app.include_router(gateway.router, prefix="/v2")
