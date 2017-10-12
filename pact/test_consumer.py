import atexit
import unittest

from pact import Consumer, Provider
from consumer import user

pact = Consumer('Consumer').has_pact_with(Provider('Provider'))  
pact.start_service()
atexit.register(pact.stop_service)

class ContractTest(unittest.TestCase):

    def test_first(self):
        expected = {'hello': 'verification_glasses'}

        (pact
         .given('')
         .upon_receiving('a request for users with input verification_glasses')
         .with_request('get', '/users/verification_glasses')
         .will_respond_with(200, body=expected))

        gateway = 'http://localhost:1234'
        with pact:
            result = user(gateway, 'verification_glasses')
        self.assertEqual(result, expected)
