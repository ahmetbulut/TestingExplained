__author__ = 'ahmetbulut'
__date__ = "Nov 2019"

import unittest
from source import mymodule

class MyTest(unittest.TestCase):
    def test_take_square_greater(self):
        self.assertGreater(mymodule.take_square(2), 2)

    def test_take_square_equality(self):
        self.assertEqual(mymodule.take_square(1), 1)
        self.assertEqual(mymodule.take_square(0), 0)

    def test_hello_world(self):
        self.assertEqual(mymodule.hello_world(), "hello beautiful world")