# Based on the example from http://hypothesis.readthedocs.io/en/latest/examples.html#fuzzing-an-http-api
import unittest
from hypothesis import given, assume, settings, strategies as st
from collections import namedtuple
import requests
import os
import random
import time
import math
import json

# These tests will be quite slow because we have to talk to an external
# service. Also we'll put in a sleep between calls so as to not hammer it.
# As a result we reduce the number of test cases and turn off the timeout.
#settings.default.max_examples = 100
#settings.default.timeout = -1

Star = namedtuple("Star", ("slug",))

StarData = st.fixed_dictionaries({
    'name': st.text(),
    'distance': st.one_of(st.none(), st.floats())
})


class StarTest(unittest.TestCase):

    @given(StarData)
    def test_create_goal_dry_run(self, data):
        # We want slug to be unique for each run so that multiple test runs
        # don't interfere with each other. If for some reason some slugs trigger
        # an error and others don't we'll get a Flaky error, but that's OK.
        random.seed()
        slug = hex(random.getrandbits(32))[2:]

        # Use assume to guide us through validation we know about, otherwise
        # we'll spend a lot of time generating boring examples.

        # Title must not be empty
        assume(data["name"])

        # Exactly two of these values should be not None. The other will be
        # inferred by the API.

        #assume(len([1 for k in needs2 if data[k] is not None]) == 2)
        #for v in data.values():
        #    if isinstance(v, float):
        #        assume(not math.isnan(v))
        data["slug"] = slug

        # The API nicely supports a dry run option, which means we don't have
        # to worry about the user account being spammed with lots of fake goals
        # Otherwise we would have to make sure we cleaned up after ourselves
        # in this test.
        for d, v in data.items():
            if v is None:
                data[d] = "null"
            else:
                data[d] = str(v)
        headers = {"Content-type": "application/json"}
        result = requests.post(
            "http://localhost:5000/star", data=json.dumps(data), headers=headers)

        # Lets not hammer the API too badly. This will of course make the
        # tests even slower than they otherwise would have been, but that's
        # life.
        time.sleep(1.0)

        # For the moment all we're testing is that this doesn't generate an
        # internal error. If we didn't use the dry run option we could have
        # then tried doing more with the result, but this is a good start.
        self.assertNotEqual(result.status_code, 500)
        if result.status_code == 400:
            print("data: " + str(data))
            print("headers: " + str(headers))
        self.assertNotEqual(result.status_code, 400)

if __name__ == '__main__':
    unittest.main()

