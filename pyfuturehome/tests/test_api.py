from unittest import TestCase
from pyfuturehome import Api

class TestApi(TestCase):
    __api = False
    def __init__(self, *args, **kwargs):

        # @todo Secrets - put somewhere else
        username = 'xxx'
        password = 'xxx'
        url = 'https://xxx/'

        self.__api = Api(url=url, username=username, password=password)
        super(TestApi, self).__init__(*args, **kwargs)


    def test_get_token(self):
        o = self.__api
        b = o.get_token()
        self.assertTrue(b)

        b = self.__api.check_token()
        self.assertTrue(b)
