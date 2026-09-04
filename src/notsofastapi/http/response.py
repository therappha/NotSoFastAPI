"""HttpResponse class, responsible for handle response parsing"""

from notsofastapi.http.typing import HttpStatus


class HttpResponse:
    """Represents an http response"""

    def __init__(self, body: str = None, headers: dict = None, status=200):

        self.version: str = "HTTP/1.1"
        self.status: HttpStatus = status
        self.body: bytes = None
        self.headers: dict = {}

        if body:
            self.body = body.encode("utf-8")
            self.headers["Content-Length"] = len(self.body)
            self.headers["Content-Type"] = "application/json"
        if headers:
            for key, value in headers.items():
                self.headers[key] = value
