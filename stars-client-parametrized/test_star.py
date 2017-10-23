import atexit
import pytest

from pact import Consumer, Provider
from star import star

pact = Consumer('Consumer').has_pact_with(Provider('Provider'))  
pact.start_service()
atexit.register(pact.stop_service)

@pytest.mark.parametrize("expected, given, upon_receiving",
    [({'result': 'No such name'},'no_stars','a request for a star which is not in the db'),
     ({'result': {'distance': 8.6, 'name': 'Sirius'}}, 'sirius', 'a request for a star that exists in the db (Sirius)')
    ]
)
def test_sirius_with_pacts(expected, given, upon_receiving):
    (pact
        .given(given)
        .upon_receiving(upon_receiving)
        .with_request('get', '/star/Sirius')
        .will_respond_with(200, body=expected))

    gateway = 'http://localhost:1234'
    with pact:
        result = star(gateway, 'Sirius')
    assert result == expected

