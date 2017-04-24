from . import APIMetadataModel
from .properties import PropertyDescriptor

class InteracaoMetadata(APIMetadataModel):
    @property
    @PropertyDescriptor.serializable('evidencia')
    def evidencias(self):
        return self.__evidencias

    @evidencias.setter
    @PropertyDescriptor.list
    def evidencias(self, val):
        self.__evidencias = val

    @property
    @PropertyDescriptor.serializable('acao')
    def acoes(self):
        return self.__acoes

    @acoes.setter
    @PropertyDescriptor.list
    def acoes(self, val):
        self.__acoes = val

    @property
    @PropertyDescriptor.serializable('gravidade')
    def gravidades(self):
        return self.__gravidades

    @gravidades.setter
    @PropertyDescriptor.list
    def gravidades(self, val):
        self.__gravidades = val
