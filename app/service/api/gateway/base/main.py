from fastapi import FastAPI
import uvicorn
from app.service.api.static.server import routes as static
from app.service.api.docs.server import routes as docs

app = FastAPI(docs_url=False, redoc_url=False)
app.include_router(router=static.router, prefix="/static")
app.include_router(router=docs.router, prefix="/docs")
