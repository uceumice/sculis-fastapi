import os
from pathlib import Path

SERVICE_DIR = Path(os.path.dirname(os.path.realpath(__file__))).parent.as_posix()

STATIC_DIR_NAME = 'static'
STATIC_DIR = os.path.join(SERVICE_DIR, STATIC_DIR_NAME)
