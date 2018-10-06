import unittest
# import os
# import sys
# sys.path.insert(0, os.path.abspath('../'))
import gcloud_functions_params
from ostruct import OpenStruct

# Mock flask request
def flask_mock_args(mock_data):
  mock_args = OpenStruct().to_dict = lambda: mock_data
  mock = OpenStruct().args = mock_args
  return mock

def flask_mock_json(mock_data):
  mock = OpenStruct().get_json = lambda: mock_data
  return mock

class TestStringMethods(unittest.TestCase):

    def test_event_to_dict(self):
        event = {'data': "eyJuYW1lIjogImV4YW1wbGUifQo="}
        context = None
        result = gcloud_functions_params.event_to_dict(event, context)
        self.assertEqual(result['name'], "example")

    def test_event_to_dict_error(self):
        event = {}
        context = None
        result = gcloud_functions_params.event_to_dict(event, context)
        self.assertEqual(result, None)

    def test_event_to_dict(self):
        flask_request = flask_mock_args({'name': 'example'})
        result = gcloud_functions_params.args_or_json_to_dict(flask_request)
        self.assertEqual(result['name'], "example")


if __name__ == '__main__':
    unittest.main()
