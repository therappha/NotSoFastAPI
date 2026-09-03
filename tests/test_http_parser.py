"""File for storing HttpParser tests"""

from notsofastapi.http import HttpParser, HttpRequest, HttpMethod


class TestHttpParser:

    get_request = (
        b"GET /api/users?active=true&page=2 HTTP/1.1\r\n"
        b"Host: localhost:8000\r\n"
        b"User-Agent: curl/8.12.1\r\n"
        b"Accept: application/json\r\n"
        b"Accept-Language: pt-BR,pt;q=0.9,en;q=0.8\r\n"
        b"Connection: keep-alive\r\n"
        b"\r\n"
        b"{test: body}"
    )

    def test_http_valid_parse_request_returns_http_request(self):
        parsed_request = HttpParser.parse_request(self.get_request)
        assert type(parsed_request) is HttpRequest

    def test_http_request_returns_right_method(self):
        parsed_request = HttpParser.parse_request(self.get_request)
        assert parsed_request is not None
        assert parsed_request.method == "GET"

    def test_http_request_return_right_path(self):
        parsed_request = HttpParser.parse_request(self.get_request)
        assert parsed_request is not None
        assert parsed_request.path == "/api/users"

    def test_http_request_return_right_query(self):
        parsed_request = HttpParser.parse_request(self.get_request)
        assert parsed_request is not None
        assert len(parsed_request.query) == 2
        assert parsed_request.query["active"] == "true"
        assert parsed_request.query["page"] == "2"

    def test_http_request_returns_right_version(self):
        parsed_request = HttpParser.parse_request(self.get_request)
        assert parsed_request is not None
        assert parsed_request.version == "HTTP/1.1"

    def test_http_request_return_right_headers(self):
        parsed_request = HttpParser.parse_request(self.get_request)
        assert parsed_request is not None
        assert parsed_request.headers["Host"] == "localhost:8000"
        assert parsed_request.headers["User-Agent"] == "curl/8.12.1"
        assert parsed_request.headers["Connection"] == "keep-alive"
        assert len(parsed_request.headers) == 5

    def test_http_request_return_right_body(self):
        parsed_request = HttpParser.parse_request(self.get_request)
        assert parsed_request.body == b"{test: body}"
