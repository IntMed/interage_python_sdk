from .mixins import CreateInstanceFromJsonMixin
from interage.api.exceptions import messages
from interage.api.models.properties import PropertyDescriptor


class APIModel(CreateInstanceFromJsonMixin):
    def __init__(self):
        super(APIModel, self).__init__()

    @property
    @PropertyDescriptor.serializable('id')
    def id(self):
        return self.__id

    @id.setter
    @PropertyDescriptor.integer
    def id(self, val):
        self.__id = val


class APIMetadataModel(CreateInstanceFromJsonMixin):
    pass
