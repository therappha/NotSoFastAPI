"""File for creating an HttpParser"""

from notsofastapi.http import HttpRequest, HttpMethod


class HttpParser:
    @staticmethod
    def parse_request(raw_request) -> HttpRequest | None:
        parsed_request = HttpRequest(raw_request)
        parsed_request.method = HttpParser.get_request_method(parsed_request)
        parsed_request.path = HttpParser.get_request_path(parsed_request)
        parsed_request.headers = HttpParser.get_request_headers(parsed_request)
        for line in parsed_request.decoded_request:
            print(f"'{line}'")
        return parsed_request

    @staticmethod
    def get_request_method(parsed_request) -> HttpMethod | None:
        return HttpMethod.GET

    @staticmethod
    def get_request_path(parsed_request) -> str | None:
        return None

    @staticmethod
    def get_request_headers(parsed_request) -> dict | None:
        return None

    @staticmethod
    def get_request_body(parsed_request) -> bytes | None:
        return None
