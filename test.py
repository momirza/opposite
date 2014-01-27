import unittest
from opposite import *

class TestEquality(unittest.TestCase):
    def test_equality(self):
        self.assertEqual(True, True)
        self.assertEqual(False, False)
        self.assertNotEqual(True, False)
        self.assertNotEqual(False, True)
