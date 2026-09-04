"""File for storing types"""

from enum import StrEnum, IntEnum


class HttpMethod(StrEnum):
    POST = "POST"
    GET = "GET"
    PATCH = "PATCH"
    PUT = "PUT"
    DELETE = "DELETE"
    OPTIONS = "OPTIONS"
    HEAD = "HEAD"


class HttpStatus(IntEnum):
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    NO_CONTENT = 204
    TEMPORARY_REDIRECT = 302
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405
    TOO_MANY_REQUESTS = 429
    INTERNAL_ERROR = 500
    NOT_IMPLEMENTED = 501
    BAD_GATEWAY = 502
