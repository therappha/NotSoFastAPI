"""File for creating an HttpParser"""

from notsofastapi.http import HttpRequest, HttpMethod


class HttpParser:
    @staticmethod
    def parse_request(raw_request) -> HttpRequest | None:
        parsed_request = HttpRequest(raw_request)
        parsed_request.method = HttpParser.get_request_method(parsed_request)
        parsed_request.path = HttpParser.get_request_path(parsed_request)
        parsed_request.query = HttpParser.get_request_query(parsed_request)
        parsed_request.version = HttpParser.get_request_version(parsed_request)
        parsed_request.headers = HttpParser.get_request_headers(parsed_request)
        parsed_request.body = HttpParser.get_request_body(parsed_request)
        return parsed_request

    # TODO: once we have exceptions make it raise 400 or 500
    @staticmethod
    def get_request_method(parsed_request: HttpRequest) -> HttpMethod | None:
        if len(parsed_request.decoded_request) == 0:
            return None
        first_line_splitted = parsed_request.decoded_request[0].split(" ")
        for method in HttpMethod:
            if first_line_splitted[0] == method:
                return method
        return None

    @staticmethod
    def get_request_path(parsed_request: HttpRequest) -> str | None:
        if len(parsed_request.decoded_request) == 0:
            return None
        first_line_splitted = parsed_request.decoded_request[0].split(" ")
        return first_line_splitted[1].split("?")[0]

    @staticmethod
    def get_request_query(parsed_request: HttpRequest) -> dict | None:
        query = {}
        if len(parsed_request.decoded_request) == 0:
            return query
        first_line_splitted = parsed_request.decoded_request[0].split(" ")
        if "?" not in first_line_splitted[1]:
            return query
        path, queryline = first_line_splitted[1].split("?", 1)
        args = queryline.split("&")
        for arg in args:
            if "=" not in arg:
                continue
            key, value = arg.split("=", 1)
            query[key] = value

        return query

    @staticmethod
    def get_request_headers(parsed_request: HttpRequest) -> dict | None:
        headers: dict = {}
        for request in parsed_request.decoded_request[1:]:
            if request == "":
                break
            if ":" not in request:
                continue
            key, value = request.split(":", 1)
            if key and value:
                headers[key] = value.strip()
        return headers

    def get_request_version(parsed_request: HttpRequest) -> str | None:
        if len(parsed_request.decoded_request) == 0:
            return None
        first_line_splitted = parsed_request.decoded_request[0].split(" ")
        return first_line_splitted[2]

    @staticmethod
    def get_request_body(parsed_request: HttpRequest) -> bytes | None:
        return None
