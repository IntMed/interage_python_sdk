[![PyPi version](https://img.shields.io/pypi/v/interage_python_sdk.svg)](https://pypi.python.org/pypi/interage_python_sdk)

# Interage Python SDK
SDK oficialmente mantido pela [IntMed Software](http://intmed.com.br/) para auxiliar no desenvolvimento de aplicações em Python integradas ao serviço de interações medicamentosas do sistema [Interage](http://intmed.com.br/interage/). Desenvolvido para ser simples e idiomático para Python, o SDK comunica-se com uma API RESTful via protocolo HTTPS. 

## Instalação
### PIP
Se você já tem o [Python](https://www.python.org/) em seu sistema, você pode instalar o Interage Python SDK simplesmente baixando a distribuição, descompactá-la e instalá-la da maneira usual:
```
pip install interage_python_sdk
```

## Dependências
- [Requests](https://github.com/kennethreitz/requests) - O Interage Python SDK necessita que o pacote esteja instalado

## Quick Start
Para começar, instale o Interage Python SDK, crie um objeto `InterageAPI` passando o seu token para o argumento `auth` e invoque seus métodos:

```python
from interage.api import InterageAPI

api = InterageAPI(auth = 'your-api-token')
medicamentos = api.medicamentos.filter(search = 'acido').objects()

for m in medicamentos:
    print(m.nome)
```

Você também pode criar um objeto `InterageAPI` passando as suas credenciais (`username` e `password`) da API na forma de [dicionário](https://docs.python.org/2/tutorial/datastructures.html#dictionaries) para o argumento `auth`:
```python
client = InterageAPI(auth = { 'username': 'your-username', 'password': 'your-password'})
```

Qualquer credencial inválida passada no construtor de `InterageAPI` lançará uma exceção e o objeto não será criado.

### Managers
Um objeto `InterageAPI` contém referências para três objetos do tipo `APIManager`, que são basicamente gerenciadores de recursos mantidos pela API. São eles:
- `medicamentos` - Gerenciador dos recursos responsáveis pelos dados de medicamentos. Recurso `/v1/medicamentos/`
- `principios_ativos` - Gerenciador dos recursos responsáveis pelos dados de princípios ativos. Recurso `/v1/principios-ativos/`
- `interacoes` - Gerenciador dos recursos responsáveis pelos dados de interações medicamentosas entre princípios ativos. Recurso `/v1/interacoes/`

Estes gerenciadores são capazes de recuperar, listar e filtrar dados específicos da API:

```python
api.medicamentos.get(145) # Retorna o medicamento com o identificador (id) 145
api.principios_ativos.all() # Lista todos os princípios ativos do sistema
api.interacoes.filter(principios_ativos = [17, 443, 648, 1200], gravidade = 'grave')  # Retorna todas as interações medicamentosas graves entre os principios ativos com os identificadores 17, 443, 648 e 1200
```

Os managers `principios_ativos` e `interacoes` contém comportamento extra. O manager `principios_ativos` é capaz de recuperar todas as interações medicamentosas que um princípio ativo específico possua:
```python
api.principios_ativos.interacoes(1) # Retorna todas as interações encontradas com o princípio ativo de identificador (id) igual a 1
```
No manager `interacoes` é possível verificar todos os metadados referentes a uma interação medicamentosa. O método retorna um objeto do tipo `InteracaoMetadata`', mas também pode retornar o resultado como JSON:

```python
metadata = api.interacoes.metadata()

print(metadata.gravidades) # ['Nada esperado', 'Moderada', 'Leve', 'Grave', 'Gravidade desconhecida']
print(metadata.evidencias) # ['Teórica', 'Extensa', 'Caso', 'Estudo']
print(metadata.acoes) # ['Ajustar', 'Monitorar', 'Informar', 'Nenhuma', 'Evitar']
```

### Tipos de retorno e paginação
Os métodos dos managers que retornam mais de um resultado (`all()` e `filter()`) são encapsulados em um objeto do tipo `APIResult`. Este objeto é capaz de retornar os resultados fornecidos pela API como JSON ou como lista de instâncias das classes `PrincipioAtivo`, `Medicamento` ou `Interacao` através dos métodos, reespectivamente, `json()` e `objects()`:

```python
results = api.medicamentos.all()
medicamentos = results.objects() # Lista de instâncias da classe Medicamento
medicamentos_json = results.json() # JSON com lista de medicamentos

for m in medicamentos:
    print(m.nome)
 
for m in medicamentos_json:
    print(m['nome'])
```

Os métodos de managers que retornam resultado único retornam por default uma instância do modelo referente ao manager. Caso necessite que o objeto seja retornado como JSON, basta passar o valor `True` para o argumento `as_json`:
```python
principio_ativo = api.principios_ativos.get(5)
principio_ativo_json = api.principios_ativos.get(5, as_json = True)

print(principio_ativo.nome)
print(principio_ativo_json['nome'])
```
Os resultados em um `APIResult` são paginados de acordo com os parâmetros passados aos métodos dos managers. Através dos métodos `next()` e `previous()` são retornados uma nova instância de `APIResult` referentes a página posterior e anterior do resultado corrente, reespectivamente. Os métodos `has_next()` e `has_previous()` podem ajudar a saber se as referências para estas páginas existem:

```python
result = api.principios_ativos.filter(search = 'ra', page_size = 50)
while(result.has_next()):
    objects = result.objects()
    for i in range(len(objects)):
        print(objects[i].nome)
    result = result.next()
```
## Reportando problemas
Se você tem sugestões, bugs ou outros tipos de problemas com este SDK, esteja livre para reportar [aqui](https://github.com/weynelucas/interage_python_sdk/issues). Ou simplesmente envie um pull request.

## API
Para mais dúvidas sobre os parâmetros, endpoints, criação de tokens e outras dúvidas sobre a API, consulte a documentação oficial da API do Interage [aqui]( https://api.interage.intmed.com.br/docs/).

## Versão
- 0.1.0 - 27/02/2017 - Primeira release
- 0.1.1 - 27/02/2017 - Correção de erro crash do pacote utils e mudança de protocolo para HTTPS
- 0.2.0 - 01/03/2017 - Suporte para paginação e adição do campo principios_ativos_anvisa em medicamentos
- 0.2.1 - 02/03/2017 - Correção de instanciações de managers desnecessárias em um mesmo client
- 0.2.2 - 04/03/2017 - Melhorias de código e mudança de responsabilidade dos managers para InterageAPI
- 0.2.3 - 09/03/2017 - Melhoria no tratamento de erros HTTP
- 0.3.0 - 24/04/2017 - Melhoria substancial na conversão de JSON em objetos
