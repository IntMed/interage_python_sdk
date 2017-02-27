from . import consts
from interage.api.utils.strings import remove_lead_and_trail_slash

class APIUri:
    medicines = consts.MEDICINES_URI
    interactions = consts.INTERACTIONS_URI
    active_principles = consts.ACTIVE_PRINCIPLES_URI
    obtain_token = consts.OBTAIN_TOKEN_URI
    metadata = consts.METADATA

class APIInteractionsMetadata:
    actions    = consts.INTERACTION_ACTIONS
    evidences  = consts.INTERACTION_EVIDENCES
    severities = consts.INTERACTION_SEVERITIES

class APISettings:
    uris                  = APIUri
    url                   = consts.API_URL
    version               = consts.VERSION
    auth_keys             = consts.AUTH_KEYS
    interactions_metadata = APIInteractionsMetadata

    @classmethod
    def get_full_url(self, uri, append_version = True):
        uri = remove_lead_and_trail_slash(uri)

        url = self.url
        version = self.version

        if(append_version):
            result = '{0}/{1}/{2}'.format(url, version, uri)
        else :
            result = '{0}/{1}'.format(url, uri)

        if(len(uri)):
            result += '/'

        return result


    @classmethod
    def register_token(self, token):
        self.token = token
