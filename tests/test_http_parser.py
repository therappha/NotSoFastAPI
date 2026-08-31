"""File for storing HttpParser tests"""

from notsofastapi.http import HttpParser, HttpRequest, HttpMethod


class TestHttpParser:

    def test_http_valid_parse_request_returns_http_request(self):
        request = HttpParser.parse_request(b"GET / HTTP/1.1\r\n")
        assert type(request) is HttpRequest
