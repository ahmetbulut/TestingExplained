__author__ = 'ahmetbulut'

import unittest
from source import mymodule

class MyTest(unittest.TestCase):
    def test_xyz(self):
        assert 2 == 2

    def test_hello_world(self):
        self.assertEqual(mymodule.hello_world(), "hello beautiful world")
