from fastapi.responses import StreamingResponse
from fastapi import BackgroundTasks

from typing import Union
from io import BufferedReader, BytesIO
import os


class FileResponse(StreamingResponse):
    def __init__(self, content_or_path: Union[BufferedReader, bytes, "os.PathLike"], status_code: int = 200, headers: dict = None, media_type: str = None, background: BackgroundTasks = None) -> None:
        content: bytes
        if isinstance(content_or_path, BufferedReader):
            content = BytesIO(content_or_path.read())

        elif isinstance(content_or_path, str):
            try:
                with open(content_or_path, 'rb') as f:
                    content = BytesIO(f.read())
            except Exception as error:
                raise error

        elif isinstance(content_or_path, BytesIO):
            content = content_or_path
        else:
            content = BytesIO(content_or_path)

        super().__init__(content, status_code, headers, media_type, background)


class PngResponse(FileResponse):
    def __init__(self, content: bytes, status_code: int = 200, headers: dict = None, media_type: str = None, background: BackgroundTasks = None) -> None:
        super().__init__(content, status_code, headers, "image/png", background)


class SvgResponse(FileResponse):
    def __init__(self, content: bytes, status_code: int = 200, headers: dict = None, media_type: str = None, background: BackgroundTasks = None) -> None:
        super().__init__(content, status_code, headers, "media/svg+xml", background)


class IcoResponse(FileResponse):
    def __init__(self, content: bytes, status_code: int = 200, headers: dict = None, media_type: str = None, background: BackgroundTasks = None) -> None:
        super().__init__(content, status_code, headers, "image/x-icon", background)
