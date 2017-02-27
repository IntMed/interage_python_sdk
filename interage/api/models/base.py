from .mixins import CreateInstanceFromJsonMixin
from interage.api.exceptions import messages
from interage.api.models.properties import PropertyDescriptor


class APIModel(CreateInstanceFromJsonMixin):
    def __init__(self):
        super(APIModel, self).__init__()

    @property
    def id(self):
        return self.__id

    @id.setter
    @PropertyDescriptor.integer
    def id(self, val):
        self.__id = val


class APIMetadataModel(CreateInstanceFromJsonMixin):
    pass


def json_to_instance_list(model, json):
    if(issubclass(model, CreateInstanceFromJsonMixin)):
        return [model.create_instance_from_json(record) for record in json]

    raise AttributeError(messages.arg_issubclass_error.format('model', CreateInstanceFromJsonMixin.__name__))
