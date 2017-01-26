import unittest
from app import app
from pprint import pprint
from flask import jsonify
import json

class FlaskTest(unittest.TestCase):

    def setUp(self):
        self.app=app.test_client()

    def tearDown(self):
        pass

    def test_root(self):
        rv=self.app.get('/')
        expected_value = {"project": "bistro","version": "1.0.0"}
        actual_value = json.loads(rv.data)
        self.assertDictEqual(expected_value, actual_value, "Check that the response is structurally equal")

