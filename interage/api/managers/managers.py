from interage.api import models
from interage.api.config import APISettings
from .base import APIManager
from .mixins import APIManagerMetadataMixin, APIManagerInteracoesMixin
from interage.api.models.metadata import InteracaoMetadata

class PrincipioAtivoAPIManager(APIManager, APIManagerInteracoesMixin):
    uri = APISettings.uris.active_principles
    model_class = models.PrincipioAtivo

class MedicamentoAPIManager(APIManager):
    uri = APISettings.uris.medicines
    model_class = models.Medicamento

class InteracaoAPIManager(APIManager, APIManagerMetadataMixin):
    uri = APISettings.uris.interactions
    model_class = models.Interacao
    metadata_class = InteracaoMetadata
