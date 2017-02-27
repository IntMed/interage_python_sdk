from abc import ABCMeta
from interage.api import models
from interage.api.config import APISettings

class APIManager(metaclass = ABCMeta):
    def __init__(self, **args):
        super(APIManager, self).__init__()
        self.client = args.get('client')

    def get(self, id, as_json = False):
        result = self.client.request(self.uri + str(id))
        return self.__handle_result(result, as_json)

    def all(self, as_json = False):
        result =  models.APIJsonResult(self.client.request(self.uri))
        return self.__handle_result(result, as_json)

    def filter(self, **params):
        as_json = params.get('as_json', False)
        result = models.APIJsonResult(self.client.request(self.uri, params = params))
        return self.__handle_result(result, as_json)

    def __handle_result(self, result, as_json):
        if(not as_json):
            if(isinstance(result, models.APIJsonResult)):
                result = result.to_instance_list(self.model_class)
            else:
                result = self.model_class.create_instance_from_json(result)

        return result
