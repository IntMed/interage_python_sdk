from interage.api.utils.models import json_to_instance_list, list_api_model_properties

class CreateInstanceFromJsonMixin:
    serializable_attrs = ['serializable_name', 'serializable_ref']

    @classmethod
    def create_instance_from_json(cls, json):
        instance = cls()
        properties = list_api_model_properties(cls)
        for p in properties:
            if(cls.__has_serializable_properties):
                serializable_ref = p.fget.serializable_ref
                serializable_name = p.fget.serializable_name

                if(serializable_ref is None):
                    p.fset(instance, json[serializable_name])
                else:
                    content = json[serializable_name]
                    if(isinstance(content, list)):
                        p.fset(instance, json_to_instance_list(serializable_ref, content))

        return instance

    @classmethod
    def __has_serializable_properties(cls, prop):
        return all([hasattr(prop.fget, attr) for attr in cls.serializable_attrs])
