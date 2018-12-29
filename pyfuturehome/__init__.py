import requests
import json

class Api():
    __baseurl = ''
    __username = ''
    __password = ''
    __access_token = ''

    def __init__(self, url = '', username = '', password = ''):
        self.__baseurl = url
        self.__username = username
        self.__password = password


    def get_token(self):
        '''
        Setup access token using username/password
        '''

        url = self.__baseurl + 'v1/oauth/access_token'
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        payload = {
            'grant_type': 'password',
            'username': self.__username,
            'password': self.__password,
            'client_id': 'G8SliLCuGgHBqOn7',
            'client_secret': '1fdUB4mtydYEOTRrdfY24YySRfEOFzxe',
        }

        r = requests.post(
            url,
            headers = headers,
            data=payload
        )

        if r.status_code != 200:
            return False

        data = json.loads(r.text)
        self.__access_token = data['access_token']

        return True


    def check_token(self):
        '''
        Check validity of access token
        '''

        url = self.__baseurl + 'v1/oauth/check'
        bearer = 'Bearer ' + self.__access_token
        headers = {
            'content-type': 'application/x-www-form-urlencoded',
            'authorization': bearer,
        }
        r = requests.get(
            url,
            headers = headers,
        )

        if r.status_code == 200:
            return True

        return False
