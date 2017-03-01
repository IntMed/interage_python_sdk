from interage.api.config import APISettings
from interage.api.exceptions import HttpNotFoundError
from .base import json_to_instance_list


class APIResult(object):
    def __init__(self, **args):
        super(APIResult, self).__init__()
        self.client = args.get('client')
        self.model_class = args.get('model_class')
        self.__load_from_response(args.get('response'))

    def __load_from_response(self, response):
        self.__count    = response.get('count', 0)
        self.__results  = response.get('results', [])
        self.__next     = response.get('next', None)
        self.__previous = response.get('previous', None)

    def __get_result_object(self, result):
        return APIResult(
            response = result,
            client = self.client,
            model_class = self.model_class,
        )

    def has_next(self):
        return self.__next is not None

    def has_previous(self):
        return self.__previous is not None

    def next(self):
        if(self.has_next):
            result = self.client.request(self.__next)
            return self.__get_result_object(result)

        raise HttpNotFoundError()

    def previous(self):
        if(self.has_previous):
            result = self.client.request(self.__previous)
            return self.__get_result_object(result)

        raise HttpNotFoundError()

    def results(self, as_json = False):
        if(as_json):
            return self.__results

        return json_to_instance_list(self.model_class, self.__results)

    @property
    def count(self):
        return self.__count
