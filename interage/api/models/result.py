from interage.api.config import APISettings
from interage.api.exceptions import HttpNotFoundError
from .base import json_to_instance_list


class APIResult(object):
    def __init__(self, **args):
        super(APIResult, self).__init__()
        self.client = args.get('client')
        self.model_class = args.get('model_class')
        self.__load_from_response(args.get('response'))

    def __load_from_response(response):
        self.__count    = response.get('count', 0)
        self.__results  = response.get('results', [])
        self.__next     = response.get('next', None)
        self.__previous = response.get('previous', None)

    def has_next(self):
        return self.__next is not None

    def has_previous(self):
        return self.__previous is not None

    def next(self):
        if(self.has_next):
            response = client.request(get_uri_from_full_url(self.__next))
            return APIResult(client = self.client, model_class = self.model_class, response = response)

        raise HttpNotFoundError()

    def previous(self):
        if(self.has_previous):
            response = client.request(get_uri_from_full_url(self.__previous))
            return APIResult(client = self.client, model_class = self.model_class, response = response)

        raise HttpNotFoundError()

    def results(self, as_json = False):
        if(as_json):
            return self.results

        return json_to_instance_list(self.model_class, self.__results)

    @property
    def count(self):
        return self.__count



def get_uri_from_full_url(url):
    return url.replace(APISettings.url + '/' + APISettings.version + '/', '')
