from interage.api.client import APIClient

class InterageAPI:
    @classmethod
    def client(self, **args):
        return APIClient(**args)
