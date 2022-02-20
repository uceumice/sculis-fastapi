import os
from pathlib import Path

SERVER_DIR = Path(os.path.dirname(
    os.path.realpath(__file__))).as_posix()
CLIENT_DIR = Path(SERVER_DIR).as_posix()


BUILD_DIR = os.path.join(CLIENT_DIR, 'build')
STATIC_DIR = os.path.join(BUILD_DIR, 'static')

HTML_DIR = BUILD_DIR
