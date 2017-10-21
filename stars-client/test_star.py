import atexit
import unittest

from pact import Consumer, Provider
from star import star

pact = Consumer('Consumer').has_pact_with(Provider('Provider'))  
pact.start_service()
atexit.register(pact.stop_service)

class ContractTest(unittest.TestCase):

    def test_no_star_with_name(self):
        expected = {'result': 'No such name'}

        (pact
         .given('no_stars')
         .upon_receiving('a request a star which is not in the db')
         .with_request('get', '/star/Sirius')
         .will_respond_with(200, body=expected))

        gateway = 'http://localhost:1234'
        with pact:
            result = star(gateway, 'Sirius')
        self.assertEqual(result, expected)

    def test_start_found(self):
        expected = {'result': {'distance': 8.6, 'name': 'Sirius'}}

        (pact
         .given('sirius')
         .upon_receiving('a request for a star that exists in the db (Sirius)')
         .with_request('get', '/star/Sirius')
         .will_respond_with(200, body=expected))

        gateway = 'http://localhost:1234'
        with pact:
            result = star(gateway, 'Sirius')
        self.assertEqual(result, expected)
