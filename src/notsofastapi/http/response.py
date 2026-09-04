"""HttpResponse class, responsible for handle response parsing"""

from notsofastapi.http.typing import HttpStatus


class HttpResponse:
    """Represents an http response"""

    def __init__(self, body: str = None, headers: dict = None, status: int = 200):

        self.version: str = "HTTP/1.1"
        self.status: HttpStatus = HttpStatus(status)
        self.body: bytes = None
        self.headers: dict = {}

        if body:
            self.body = body.encode("utf-8")
            self.headers["Content-Length"] = len(self.body)
            self.headers["Content-Type"] = "application/json"
        if headers:
            for key, value in headers.items():
                self.headers[key] = value

    def encode_headers(self) -> bytes:
        header_bytes = b""

        for key, value in self.headers.items():
            header_bytes += f"{key}: {value}\r\n".encode("utf-8")

        return header_bytes

    def encode_response(self) -> bytes:
        response = b""

        http_line = f"{self.version} {self.status.value} {self.status.name}\r\n".encode(
            "utf-8"
        )
        header_bytes = self.encode_headers()

        response += http_line
        if header_bytes != b"":
            response += header_bytes
        response += "\r\n".encode("utf-8")
        if self.body is not None:
            response += self.body
        return response
