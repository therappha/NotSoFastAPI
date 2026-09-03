"""HttpRequest class, for handling request parsing"""


class HttpRequest:
    """Represents an HttpRequest"""

    def __init__(self, request):
        self.raw_request: bytes = request
        self.decoded_request: str = request.decode("utf-8").splitlines()

        # Declaring variables for type hinting
        self.method: str = None
        self.path: str = None
        self.query: dict = None
        self.version: str = None
        self.headers: dict = None
        self.body: bytes = None
