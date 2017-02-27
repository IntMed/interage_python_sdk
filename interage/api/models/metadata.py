from . import APIMetadataModel
from .properties import PropertyDescriptor

class InteracaoMetadata(APIMetadataModel):
    @property
    def evidencias(self):
        return self.__evidencias

    @evidencias.setter
    @PropertyDescriptor.list
    def evidencias(self, val):
        self.__evidencias = val

    @property
    def acoes(self):
        return self.__acoes

    @acoes.setter
    @PropertyDescriptor.list
    def acoes(self, val):
        self.__acoes = val

    @property
    def gravidades(self):
        return self.__gravidades

    @gravidades.setter
    @PropertyDescriptor.list
    def gravidades(self, val):
        self.__gravidades = val

    @classmethod
    def create_instance_from_json(self, json):
        instance = InteracaoMetadata()
        instance.evidencias = json['evidencia']
        instance.acoes = json['acao']
        instance.gravidades = json['gravidade']

        return instance
