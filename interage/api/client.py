import requests
from interage.api.config import APISettings
from interage.api.exceptions import messages
from interage.api.exceptions import get_http_error
from interage.api import managers

class APIClient(object):
    def __init__(self, **args):
        super(APIClient, self).__init__()
        self.url = args.get('url', APISettings.url)
        self.__handle_auth(args.get('auth'))

    def __handle_auth(self, auth):
        if(auth is None):
            raise AttributeError(messages.empty_arg_error.format('auth'))

        if(isinstance(auth, dict)):
            if(any([key in APISettings.auth_keys for key in auth])):
                self.token = self.__obtain_token(auth)
            else:
                raise AttributeError(messages.invalid_key_arg_error.format('auth', APISettings.auth_keys))
        else:
            self.token = auth
            self.request()

    def __handle_http_error(self, response):
        error = get_http_error(response)

        if(error is not None):
            raise error(response)

    def __obtain_token(self, auth):
        response = requests.post(APISettings.get_full_url(APISettings.uris.obtain_token, append_version = False), data = auth)
        self.__handle_http_error(response)
        return response.json()['token']


    def request(self, url = '', params = None):
        if(APISettings.url not in url):
            url = APISettings.get_full_url(url)

        response = requests.get(url, headers = { 'Authorization': 'Token ' + self.token }, params = params)
        self.__handle_http_error(response)
        return response.json()
