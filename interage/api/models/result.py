from interage.api.config import APISettings
from interage.api.exceptions import HttpNotFoundError
from interage.api.utils.models import json_to_instance_list


class APIResult(object):
    def __init__(self, **args):
        super(APIResult, self).__init__()
        self.client = args.get('client')
        self.model_class = args.get('model_class')
        self._load_from_response(args.get('response'))

    def _load_from_response(self, response):
        self._count    = response.get('count', 0)
        self._results  = response.get('results', [])
        self._next     = response.get('next', None)
        self._previous = response.get('previous', None)

    def _get_result_object(self, result):
        return APIResult(
            response = result,
            client = self.client,
            model_class = self.model_class,
        )

    def has_next(self):
        return self._next is not None

    def has_previous(self):
        return self._previous is not None

    def next(self):
        if(self.has_next):
            result = self.client.request(self.next_url)
            return self._get_result_object(result)

        raise HttpNotFoundError()

    def previous(self):
        if(self.has_previous):
            result = self.client.request(self.previous_url)
            return self._get_result_object(result)

        raise HttpNotFoundError()
    
    @property
    def next_url(self):
        return self._next
    
    @property
    def previous_url(self):
        return self._previous     

    @property
    def count(self):
        return self._count

    def json(self):
        return self.results(as_json = True)

    def objects(self):
        return self.results(as_json = False)

    def results(self, as_json):
        if(as_json):
            return self._results
        return json_to_instance_list(self.model_class, self._results)