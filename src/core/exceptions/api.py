from rest_framework import status
from rest_framework.exceptions import APIException


class ApiBaseException(APIException):
    status_code = None
    default_detail = "Detail"
    default_code = "default code"

    def __init__(self, message=None, **kwargs):
        if message is not None:
            self.detail = message
        else:
            self.detail = self.default_detail
        self.extra = kwargs
        super().__init__(detail=self.detail)

    def get_full_details(self):
        return dict(self.extra, message=self.detail, type=self.__class__.__name__)


class NotFoundException(ApiBaseException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "Not found exception"
    default_code = "not found"


class ConflictException(ApiBaseException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = "Conflict exception"
    default_code = "conflict"
