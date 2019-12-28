from . import Base
import requests


class Users(Base):
    def __init__(self, bot_token, version='v6'):
        super().__init__(bot_token, 'user', version, )

    def self_info(self):
        response = requests.get(
            self.base_URL + '/' + self.version + '/' + '/users/@me',
            headers=self.headers,
        )
        if response.status_code == 200:
            print('success')
            print(response.status_code)
            return response.json()
        else:
            print('error')
            print(response)
            return response
