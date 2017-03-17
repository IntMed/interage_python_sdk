class CreateInstanceFromJsonMixin:
    serializable_attrs = ['serializable_name', 'serializable_ref']
    @classmethod
    def create_instance_from_json(cls, json):
        instance = cls()
        properties = [prop for name, prop in cls.__dict__.items() if isinstance(prop, property)]
        for p in properties:
            if(cls.__has_serializable_properties):
                serializable_ref = p.fget.serializable_ref
                serializable_name = p.fget.serializable_name

                if(serializable_ref is None)
                    p.fset(instance, json[serializable_name])
                else:
                    p.fset(instance, serializable_ref.create_instance_from_json(json[serializable_name]))

    @classmethod
    def __has_serializable_properties(cls, prop):
        return all([hasattr(prop.fget, attr) for attr in cls.serializable_attrs])
