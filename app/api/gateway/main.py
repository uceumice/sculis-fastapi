from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.gateway.base import router as base


origins = [
    "http://sculis.uceumice.com",
    "https://sculis.uceumice.com",
    "https://sculis-api.uceumice.com",
    "http://sculis-web.herokuapp.com",
    # "http://127.0.0.1:3000",
    # "http://localhost:3000"
]

app = FastAPI(
    debug=True,
    title="Sculis API Gateway",
    description="""
*Vertretung / Stundenplan. Alles in einem API! 🚀*
""",
    version="alpha",
    terms_of_service="/tos#api",
    contact={'Alex': "alexandrutocar@gmail.com"},
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.include_router(base.router, prefix="/b/v2")

# TODO
# app.include_router(mobile_gateway.router, prefix="/m")
# app.include_router(desktop_gateway.router, prefix="/d")
# app.include_router(dapp_gateway.router, prefix="/a")
