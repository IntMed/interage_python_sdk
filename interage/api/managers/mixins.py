from interage.api.config import APISettings
from interage.api.models import Interacao, APIResult

class APIManagerMetadataMixin:
    def metadata(self, as_json = False):
        result = self.client.request(self.uri + APISettings.uris.metadata)
        if(as_json):
            return result

        return self.metadata_class.create_instance_from_json(result)


class APIManagerInteracoesMixin:
    def interacoes(self, id, **params):
        as_json = params.get('as_json', False)
        result = self.client.request(self.uri + str(id) + '/' + APISettings.uris.interactions, params = params)
        return APIResult(
            response = result,
            client = self.client,
            model_class = Interacao,
        )
