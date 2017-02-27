from .base import APIModel, json_to_instance_list
from .properties import PropertyDescriptor, APIPropertyDescriptor
from interage.api.config import APISettings

class PrincipioAtivo(APIModel):
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    @PropertyDescriptor.string
    def nome(self, val):
        self.__nome = val

    @classmethod
    def create_instance_from_json(cls, json):
        instance = PrincipioAtivo()
        instance.id = json['id']
        instance.nome = json['nome']

        return instance


class Medicamento(APIModel):
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    @PropertyDescriptor.string
    def nome(self, val):
        self.__nome = val

    @property
    def principios_ativos(self):
        return self.__principios_ativos

    @principios_ativos.setter
    @PropertyDescriptor.list
    def principios_ativos(self, val):
        self.__principios_ativos = val

    @classmethod
    def create_instance_from_json(cls, json):
        instance = Medicamento()
        instance.id = json['id']
        instance.nome = json['nome']
        instance.principios_ativos = json_to_instance_list(PrincipioAtivo, json['principios_ativos'])

        return instance


class Interacao(APIModel):
    @property
    def evidencia(self):
        return self.__evidencia

    @evidencia.setter
    @APIPropertyDescriptor.evidence
    def evidencia(self, val):
        self.__evidencia = val

    @property
    def acao(self):
        return self.__acao

    @acao.setter
    @APIPropertyDescriptor.action
    def acao(self, val):
        self.__acao = val

    @property
    def gravidade(self):
        return self.__gravidade

    @gravidade.setter
    @APIPropertyDescriptor.severity
    def gravidade(self, val):
        self.__gravidade = val

    @property
    def principios_ativos(self):
        return self.__principios_ativos

    @principios_ativos.setter
    @PropertyDescriptor.list
    def principios_ativos(self, val):
        self.__principios_ativos = val

    @classmethod
    def create_instance_from_json(cls, json):
        instance = Interacao()
        instance.id = json['id']
        instance.evidencia = json['evidencia']
        instance.acao = json['acao']
        instance.gravidade = json['gravidade']
        instance.principios_ativos = json_to_instance_list(PrincipioAtivo, json['principios_ativos'])

        return instance
