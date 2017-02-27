# Interage Python SDK
SDK oficialmente mantido pela [IntMed Software](http://intmed.com.br/) para auxiliar no desenvolvimento de aplicações em Python integradas ao serviço de interações medicamentosas do sistema Interage. Desenvolvido para ser simples e idiomático para Python, o SDK se comunica com uma API RESTful através de um protocolo HTTP.

A documentação oficial da API pode ser encontrada em http://api.interage.intmed.com.br/docs/ 

## Instalação
### PIP
Se você já tem o [Python](https://www.python.org/) em seu sistema, você pode instalar o Interage Python SDK simplesmente baixando a distribuição, descompactá-la e instalá-la da maneira usual:
```
pip install interage_python_sdk
```

## Dependências
- [Requests](https://github.com/kennethreitz/requests) - O Interage Python SDK necessita que o pacote esteja instalado

## Quick Start
Para começar, instale o Interage Python SDK, crie um objeto `APIClient` passando o seu token para o argumento `auth` e invoque seus métodos:

```python
from interage.api import InterageAPI

client = InterageAPI.client(auth = 'your-api-token')
medicamentos = client.medicamentos.filter([search = 'acido'])

for m in medicamentos:
  print(m.nome)
```

Você também pode criar um cliente passando as suas credencias (`username` e `password`) da API na forma de [dicionário](https://docs.python.org/2/tutorial/datastructures.html#dictionaries):
```python
client = InterageAPI.client(auth = { 'username': 'your-username', 'password': 'your-password'})
```

### Managers
Um objeto `APIClient` contém referências para três objetos do tipo `APIManager`, que são basicamente gerenciadores dos dados mantidos pela API. São eles:
- `medicamentos` - Gerenciador dos dados sobre medicamentos. Endpoint '/v1/medicamentos/'
- `principios_ativos` - Gerenciador dos dados de princípios ativos. Endpoint '/v1/principios-ativos/'
- `interacoes` - Gerenciador dos dados de interações medicamentosas entre princípios ativos. Endpoint '/v1/interacoes/'

Estes gerenciadores são capazes de recuperar, listar e filtrar dados específicos da API:

```python
from interage.api import InterageAPI

client = InterageAPI.client(auth = 'your-api-token')

medicamento = client.medicamentos.get(145) # Retorna o medicamento com o identificador (id) 145
principios  = client.principios_ativos.all() # Lista todos os princípios ativos do sistema
interacoes  = client.interacoes.filter(principios_ativos= [17, 443, 648, 1200], gravidade = 'grave')  # Retorna todas as interações medicamentosas graves entre os principios ativos com os identificadores 17, 443, 648 e 1200
```

### Retornando instâncias como JSON
Os valores retornados pelos managers são instâncias dos tipos `Medicamento`, `PrincipioAtivo` e `Interacao`. Porém é possível retornar instâncias como JSONs. 

Para isso basta passar o argumento `as_json` como `True` para cada um dos métodos dos managers. Para os métodos `filter` e `all` são retornados objetos do tipo `APIJsonResult` que armazenam os dados retornados pela API como número de dados encontrados, resultados, URLs das páginas posteriores e anteriores, etc. O método `get`, por retornar apenas um item, retorna um JSON puro sem nenhum tipo de estrutura mais complexa.

```python
principios_json = client.medicamentos.filter(search = 'paracetamol', as_json = True)
print(principios_json.results)
```

## Reportando problemas
Se você tem sugestões, bugs ou otros tipos de problemas com este SDK, esteja livre para reportar [aqui](https://github.com/weynelucas/interage_python_sdk/issues). Ou simplesmente envie um pull request.

## Versão
- 0.1.0 - 27/02/2017 - Primeira release
