from interage.api.config import APISettings
from interage.api.models import Interacao, APIJsonResult

class APIManagerMetadataMixin:
    def metadata(self, as_json = False):
        result = self.client.request(self.uri + APISettings.uris.metadata)
        if(not as_json):
            result = self.metadata_class.create_instance_from_json(result)

        return result


class APIManagerInteracoesMixin:
    def interacoes(self, id, **params):
        as_json = params.get('as_json', False)
        result = APIJsonResult(self.client.request(self.uri + str(id) + '/' + APISettings.uris.interactions))
        if(not as_json):
            result = result.to_instance_list(Interacao)

        return result
