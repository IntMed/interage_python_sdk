from . import messages
from interage.api.config import APISettings

class InvalidCredentialsError(Exception):
    def __init__(self, message):
        super(InvalidCredentialsError, self).__init__(message)
        self.message = message

class HttpNotFoundError(Exception):
    message = messages.http_not_found_error
    def __init__(self, response):
        try:
            except_message = response.json()['detail']
        except:
            except_message = self.message
        finally:
            super(HttpNotFoundError, self).__init__(except_message)


class InvalidPropertyAssignmentError(AttributeError):
    message = messages.invalid_property_assignment_error
    def __init__(self, property, type):
        super(InvalidPropertyAssignmentError, self).__init__(self.message.format(property, type))

class UnknowPropertyAssignmentError(AttributeError):
    message = messages.unknow_property_assignment_error
    def __init__(self, property, objects):
        super(UnknowPropertyAssignmentError, self).__init__(self.message.format(property, objects))
