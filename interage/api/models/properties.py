from interage.api.config import APISettings
from interage.api.exceptions import InvalidPropertyAssignmentError, UnknowPropertyAssignmentError


def isinstance_wrapper(func, type):
    def wrap(instance, val):
        if(not isinstance(val, type)):
            raise InvalidPropertyAssignmentError(func.__name__, type.__name__)
        else:
            return func(instance, val)

    return wrap

def inlist_wrapper(func, objects):
    def wrap(instance, val):
        if(val not in objects):
            raise UnknowPropertyAssignmentError(func.__name__, objects)
        else:
            return func(instance, val)

    return wrap


class ClassPropertyDescriptor(object):

    def __init__(self, fget, fset=None):
        self.fget = fget
        self.fset = fset

    def __get__(self, obj, klass=None):
        if klass is None:
            klass = type(obj)
        return self.fget.__get__(obj, klass)()

    def __set__(self, obj, value):
        if not self.fset:
            raise AttributeError()
        type_ = type(obj)
        return self.fset.__get__(obj, type_)(value)

    def setter(self, func):
        if not isinstance(func, (classmethod, staticmethod)):
            func = classmethod(func)
        self.fset = func
        return self


class PropertyDescriptor:
    @classmethod
    def classproperty(cls, func):
        if not isinstance(func, (classmethod, staticmethod)):
            func = classmethod(func)

        return ClassPropertyDescriptor(func)

    @classmethod
    def integer(cls, func):
        print(func.__name__)
        return isinstance_wrapper(int)

    @classmethod
    def integer(cls, func):
        return isinstance_wrapper(func, int)

    @classmethod
    def string(cls, func):
        return isinstance_wrapper(func, str)

    @classmethod
    def list(cls, func):
        return isinstance_wrapper(func, list)


class APIPropertyDescriptor:
    @classmethod
    def evidence(cls, func):
        return inlist_wrapper(func, APISettings.interactions_metadata.evidences)

    @classmethod
    def action(cls, func):
        return inlist_wrapper(func, APISettings.interactions_metadata.actions)

    @classmethod
    def severity(cls, func):
        return inlist_wrapper(func, APISettings.interactions_metadata.severities)
