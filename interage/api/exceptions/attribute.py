from . import messages


class InvalidPropertyAssignmentError(AttributeError):
    message = messages.invalid_property_assignment_error
    def __init__(self, property, type):
        super(InvalidPropertyAssignmentError, self).__init__(self.message.format(property, type))

class UnknowPropertyAssignmentError(AttributeError):
    message = messages.unknow_property_assignment_error
    def __init__(self, property, objects):
        super(UnknowPropertyAssignmentError, self).__init__(self.message.format(property, objects))
