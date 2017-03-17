from . import APIModel
from .properties import PropertyDescriptor, APIPropertyDescriptor
from interage.api.config import APISettings

class PrincipioAtivo(APIModel):
    @property
    @PropertyDescriptor.serializable('nome')
    def nome(self):
        return self.__nome

    @nome.setter
    @PropertyDescriptor.string
    def nome(self, val):
        self.__nome = val


class Medicamento(APIModel):
    @property
    @PropertyDescriptor.serializable('nome')
    def nome(self):
        return self.__nome

    @nome.setter
    @PropertyDescriptor.string
    def nome(self, val):
        self.__nome = val

    @property
    @PropertyDescriptor.serializable('principios_ativos', PrincipioAtivo)
    def principios_ativos(self):
        return self.__principios_ativos

    @principios_ativos.setter
    @PropertyDescriptor.list
    def principios_ativos(self, val):
        self.__principios_ativos = val

    @property
    @PropertyDescriptor.serializable('principios_ativos_anvisa')
    def principios_ativos_anvisa(self):
        return self.__principios_ativos_anvisa

    @principios_ativos_anvisa.setter
    @PropertyDescriptor.list
    def principios_ativos_anvisa(self, val):
        self.__principios_ativos_anvisa = val


class Interacao(APIModel):
    @property
    @PropertyDescriptor.serializable('evidencia')
    def evidencia(self):
        return self.__evidencia

    @evidencia.setter
    @APIPropertyDescriptor.evidence
    def evidencia(self, val):
        self.__evidencia = val

    @property
    @PropertyDescriptor.serializable('acao')
    def acao(self):
        return self.__acao

    @acao.setter
    @APIPropertyDescriptor.action
    def acao(self, val):
        self.__acao = val

    @property
    @PropertyDescriptor.serializable('gravidade')
    def gravidade(self):
        return self.__gravidade

    @gravidade.setter
    @APIPropertyDescriptor.severity
    def gravidade(self, val):
        self.__gravidade = val

    @property
    @PropertyDescriptor.serializable('principios_ativos', PrincipioAtivo)
    def principios_ativos(self):
        return self.__principios_ativos

    @principios_ativos.setter
    @PropertyDescriptor.list
    def principios_ativos(self, val):
        self.__principios_ativos = val
