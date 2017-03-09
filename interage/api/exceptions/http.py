import sys
import inspect
from . import messages

class HttpError(Exception):
    response_attr = 'detail'
    def __init__(self, response):
        try:
            except_message = response.json()[self.response_attr]
            if(isinstance(except_message, list)):
                except_message = except_message[0]
        except:
            except_message = self.default_message
        finally:
            message = messages.http_error_base.format(self.status_code, except_message)
            super(HttpError, self).__init__(message)

class HttpBadRequestError(HttpError):
    status_code = 400
    response_attr = 'non_field_errors'
    default_message = messages.invalid_credentials_error

class HttpForbiddenError(HttpError):
    status_code = 403
    default_message = messages.invalid_credentials_error

class HttpNotFoundError(HttpError):
    status_code = 404
    default_message = messages.http_not_found_error

class HttpTooManyRequestsError(HttpError):
    status_code = 429
    default_message = messages.to_many_requests_error

def is_http_error_subclass(cls):
    return inspect.isclass(cls) and cls != HttpError and issubclass(cls, HttpError)

def get_http_error(response):
    module = sys.modules[__name__]
    http_errors = [cls for name, cls in module.__dict__.items() if is_http_error_subclass(cls)]
    error = list(filter(lambda err: err.status_code == response.status_code, http_errors))

    if(len(error)):
        return error[0]

    return None
