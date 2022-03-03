from fastapi import FastAPI

from app.service.api.gateway import main as gateway

# notice
# main works as a root gateway.
# as such, bot frontend at "/" and
# api at "/v2" can be deployed at the same time
# from a single uvicorn web-server (a.k.a single heroku $PORT)

app = FastAPI(docs_url=False, redoc_url=False)

app.mount("/v2", gateway.app, name="Sculis API")
