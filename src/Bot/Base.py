import requests


class Base:
    def __init__(self, bot_token, resource, version='v6'):
        self.version = version
        self.headers = {'Authorization': f'Bot {bot_token}'}
        self.base_URL = 'https://discordapp.com/api'
        self.resource = resource

    def GET(self, resource, method, *args, **kwargs):
        url = self.base_URL + '/' + self.version + '/' + f'/{resource}/{method}'
        if args:
            for a in args:
                url += f'/{a}'

        response = requests.get(
            url,
            params=kwargs,
            headers=self.headers,
        )
        return response

