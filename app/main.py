from fastapi import FastAPI

from app.service.api.gateway import main as gateway
from app.service.client.server import main as client


app = FastAPI(docs_url=False, redoc_url=False)

app.mount("/api", gateway.app, name="Sculis API")
app.mount('/', client.app, name="Sculis App")
