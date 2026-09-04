from notsofastapi.http import HttpRequest, HttpMethod, HttpResponse, HttpStatus
from abc import ABC, abstractmethod


class ApiView(ABC):

    @abstractmethod
    def post(self, request: HttpRequest) -> HttpResponse:
        pass

    @abstractmethod
    def get(self, request: HttpRequest) -> HttpResponse:
        pass

    @abstractmethod
    def list(self, request: HttpRequest) -> HttpResponse:
        pass

    @abstractmethod
    def patch(self, request: HttpRequest) -> HttpResponse:
        pass

    @abstractmethod
    def put(self, request: HttpRequest) -> HttpResponse:
        pass

    @abstractmethod
    def delete(self, request: HttpRequest) -> HttpResponse:
        pass

    @abstractmethod
    def options(self, request: HttpRequest) -> HttpResponse:
        pass

    @abstractmethod
    def head(self, request: HttpRequest) -> HttpResponse:
        pass

    @classmethod
    def _process_request(cls, request: HttpRequest) -> HttpResponse:
        allowed_methods = cls._get_allowed_methods()
        if request.method not in allowed_methods:
            return HttpResponse(status=HttpStatus.METHOD_NOT_ALLOWED)
        return getattr(cls, request.method.lower())(request)

    # TODO: remake this with list comprehension
    @classmethod
    def _get_allowed_methods(cls) -> list[str]:
        allowed_methods = []
        for name in cls.__dict__.keys():
            if name.upper() in HttpMethod:
                allowed_methods.append(name.upper())
        return allowed_methods
