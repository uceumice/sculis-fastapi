from cairosvg import svg2png
from app.service.api.logo.utils.utils import STATIC_DIR


def logo(filepath: str, size: int):
    with open(filepath, mode='r') as f:
        svg = f.read()
    return svg2png(bytestring=svg, output_width=size, output_height=size)
