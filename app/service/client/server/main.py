from fastapi.staticfiles import StaticFiles

from app.service.client.utils import BUILD_DIR


app = StaticFiles(directory=BUILD_DIR, html=True)
