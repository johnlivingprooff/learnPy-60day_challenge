import unittest
from logical_error import *

class TestLogic(unittest.TestCase):

    a = [1, 2, 3]
    b = a
    c = [1, 2, 3]

    def test_add_numbers(self):
        self.assertEqual(add_numbers(5, 4), 9)
        self.assertNotEqual(subtract_numbers(5, 4), 9)

    def test_other_assertMethods(self):
        self.assertTrue(add_numbers(5, 4) == 9)
        self.assertFalse(subtract_numbers(5, 4) == 9)

    def test_assertIs(self):
        self.assertIs(self.a, self.b) # This will pass
        self.assertIsNot(self.a, self.c) # This will pass

if __name__ == '__main__':
    unittest.main()