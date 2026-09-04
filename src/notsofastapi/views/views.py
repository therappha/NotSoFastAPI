from notsofastapi.http import HttpRequest, HttpMethod, HttpResponse
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
    def get_allowed_methods(cls) -> list[str]:
        allowed_methods = []
        for name in cls.__dict__.keys:
            if name in HttpMethod:
                allowed_methods.append(HttpMethod(name))
        return allowed_methods
