import json
from interage.api.models import APIModel,  json_to_instance_list


class APIJsonResult(object):
    def __init__(self, response):
        super(APIJsonResult, self).__init__()
        self.json     = response
        self.count    = response.get('count', 0)
        self.results  = response.get('results', [])
        self.next     = response.get('next', '')
        self.previous = response.get('previous', '')

    def __str__(self):
        return json.dumps(self.json, indent=4, sort_keys=True)

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, val):
        self.__count = int(val)

    @property
    def results(self):
        return self.__results

    @results.setter
    def results(self, val):
        self.__results = val

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, val):
        self.__next = val

    @property
    def previous(self):
        return self.__previous

    @previous.setter
    def previous(self, val):
        self.__previous = val

    @property
    def json(self):
        return self.__json

    @json.setter
    def json(self, val):
        self.__json = val

    def to_instance_list(self, model):
        return json_to_instance_list(model, self.results)
