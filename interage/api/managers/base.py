from abc import ABCMeta
from interage.api import models
from interage.api.config import APISettings

class APIManager(metaclass = ABCMeta):
    def __init__(self, **args):
        super(APIManager, self).__init__()
        self.client = args.get('client')

    def get(self, id, as_json = False):
        result = self.client.request(self.uri + str(id))
        if(as_json):
            return result

        return self.model_class.create_instance_from_json(result)

    def all(self):
        result = self.client.request(self.uri)
        return self.__get_result_object(result)

    def filter(self, **params):
        result = self.client.request(self.uri, params = params)
        return self.__get_result_object(result)

    def __get_result_object(self, result):
        return models.APIResult(
            response = result,
            client = self.client,
            model_class = self.model_class,
        )
