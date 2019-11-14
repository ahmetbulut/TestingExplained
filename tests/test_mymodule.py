__author__ = 'ahmetbulut'

import unittest
from source import mymodule

class MyTest(unittest.TestCase):
    def test_xyz(self):
	self.assertEqual(4, 4)
  
    def test_hello_world(self):
        self.assertEqual(mymodule.hello_world(), "hello beautiful world")
