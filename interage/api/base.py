from .client import APIClient
from interage.api import managers

class InterageAPI(object):
    def __init__(self, **args):
        super(InterageAPI, self).__init__()
        self.__client = APIClient(**args)
        self.__init_managers()

    def __init_managers(self):
        self.__managers = {}
        self.__managers['interacoes'] =  managers.InteracaoAPIManager(client = self.__client)
        self.__managers['medicamentos'] = managers.MedicamentoAPIManager(client = self.__client)
        self.__managers['principios_ativos'] = managers.PrincipioAtivoAPIManager(client = self.__client)

    @property
    def interacoes(self):
        return self.__managers['interacoes']

    @property
    def medicamentos(self):
        return self.__managers['medicamentos']

    @property
    def principios_ativos(self):
        return self.__managers['principios_ativos']
