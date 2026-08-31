"""HttpRequest class, for handling request parsing"""


class HttpRequest:
    """Represents an HttpRequest"""

    def __init__(self, request):
        self.raw_request = request
        self.decoded_request = request.decode("utf-8").splitlines()
