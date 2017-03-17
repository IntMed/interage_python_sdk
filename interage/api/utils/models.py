from interage.api import models
from interage.api.exceptions import messages


def json_to_instance_list(model, json):
    if(issubclass(model, models.CreateInstanceFromJsonMixin)):
        return [model.create_instance_from_json(record) for record in json]

    raise AttributeError(messages.arg_issubclass_error.format('model', CreateInstanceFromJsonMixin.__name__))


def list_properties(model_class):
    return [prop for name, prop in model_class.__dict__.items() if isinstance(prop, property)]


def list_api_model_properties(model_class):
    parent = []
    if(issubclass(model_class, models.APIModel)):
        parent = list_properties(model_class.__base__)

    child = list_properties(model_class)

    return parent + child
