import requests
from interage.api.exceptions import InvalidCredentialsError, HttpNotFoundError
from interage.api.config import APISettings
from interage.api.exceptions import messages
from interage.api import managers

class APIClient(object):
    def __init__(self, **args):
        super(APIClient, self).__init__()
        self.url = args.get('url', APISettings.url)
        self.__handle_auth(args.get('auth'))

    def request(self, uri = '', params = None):
        response = requests.get(APISettings.get_full_url(uri), headers = { 'Authorization': 'Token ' + self.token }, params = params)

        if(response.status_code == 403):
            raise InvalidCredentialsError(response.json().get('detail', messages.invalid_credentials_error))
        if(response.status_code == 404):
            raise HttpNotFoundError(response)

        return response.json()

    def obtain_token(self, auth):
        response = requests.post(APISettings.get_full_url(APISettings.uris.obtain_token, append_version = False), data = auth)

        if(response.status_code == 400):
            raise InvalidCredentialsError(response.json().get('non_field_errors', messages.invalid_credentials_error))

        return response.json()['token']

    @property
    def medicamentos(self):
        return managers.MedicamentoAPIManager(client = self)

    @property
    def principios_ativos(self):
        return managers.PrincipioAtivoAPIManager(client = self)

    @property
    def interacoes(self):
        return managers.InteracaoAPIManager(client = self)


    def __handle_auth(self, auth):
        if(auth is None):
            raise AttributeError(messages.empty_arg_error.format('auth'))

        if(isinstance(auth, dict)):
            if(any([key in APISettings.auth_keys for key in auth])):
                self.token = self.obtain_token(auth)
            else:
                raise AttributeError(messages.invalid_key_arg_error.format('auth', APISettings.auth_keys))
        else:
            self.token = auth
            self.request()
