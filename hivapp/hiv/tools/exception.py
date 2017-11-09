from hivapp import settings


def add_status_code(code):
    """
    Decorator used for adding exceptions to django_exception.
    """
    def class_decorator(cls):
        cls.status_code = code
        return cls
    return class_decorator


class WeiXinException(Exception):

    def __init__(self, code, message=None, text=None):
        Exception.__init__(self)
        self.error_code = code
        _message, _text = settings.ERROR_CODES.get(code)
        self.message = message or _message
        self.text = text or _text


@add_status_code(404)
class NotFound(WeiXinException):
    pass


@add_status_code(401)
class Unauthorized(WeiXinException):
    pass


@add_status_code(403)
class Forbidden(WeiXinException):
    pass


@add_status_code(408)
class RequestTimeout(WeiXinException):
    pass


@add_status_code(500)
class ServerError(WeiXinException):
    pass


@add_status_code(501)
class WrongInfo(WeiXinException):
    pass
