"""HttpRequest class, for handling request parsing"""


class HttpRequest:
    def __init__(self, request):
        self.raw_bytes = request
