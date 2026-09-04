from notsofastapi.http import HttpRequest, HttpMethod, HttpResponse, HttpStatus
from abc import ABC


class ApiView(ABC):

    def post(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse(status=HttpStatus.METHOD_NOT_ALLOWED)

    def get(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse(status=HttpStatus.METHOD_NOT_ALLOWED)

    def list(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse(status=HttpStatus.METHOD_NOT_ALLOWED)

    def patch(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse(status=HttpStatus.METHOD_NOT_ALLOWED)

    def put(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse(status=HttpStatus.METHOD_NOT_ALLOWED)

    def delete(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse(status=HttpStatus.METHOD_NOT_ALLOWED)

    def options(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse(status=HttpStatus.METHOD_NOT_ALLOWED)

    def head(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse(status=HttpStatus.METHOD_NOT_ALLOWED)

    def _process_request(self, request: HttpRequest) -> HttpResponse:
        allowed_methods = self._get_allowed_methods()
        if request.method not in allowed_methods:
            return HttpResponse(
                '"message": "Not Allowed"', status=HttpStatus.METHOD_NOT_ALLOWED
            )
        return getattr(self, request.method.lower())(request)

    # TODO: remake this with list comprehension
    @classmethod
    def _get_allowed_methods(cls):
        allowed_methods = []
        for name in cls.__dict__.keys():
            if name.upper() in HttpMethod:
                allowed_methods.append(name.upper())
        return allowed_methods


class MyView(ApiView):
    def get(self, request):
        return HttpResponse('"message": "get works"')

    def post(self, request):
        return HttpResponse('"message": "post works"')

    def list(self, request):
        return HttpResponse('"message": "list works"')
