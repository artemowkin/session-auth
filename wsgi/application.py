from typing import Callable

from logs import logger

from .request import WSGIRequest
from .response import handle_request


class WSGIApplication:

    """Simple WSGI application"""

    def __init__(self, environ: dict, start_response: Callable) -> None:
        self.request = WSGIRequest(environ)
        self.start_response = start_response

    def __iter__(self) -> bytes:
        response = handle_request(self.request)
        status = response.status
        response_headers = response.headers
        self.start_response(status, response_headers)
        logger.info(
            f"{self.request.get_full_path()} "
            f"{self.request.method} {status}"
        )
        yield response.body
