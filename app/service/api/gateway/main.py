from fastapi import FastAPI
from app.service.api.gateway import router as gateway
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://sculis.uceumice.com",
    "https://sculis.herokuapp.com",
    "http://127.0.0.1:3000"
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
    docs_url=False
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(gateway.router, prefix="/api")
