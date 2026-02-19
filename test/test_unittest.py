import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
from calculator import fun1, fun2, fun3, fun4

class TestCalculator(unittest.TestCase):

    def test_fun1(self):
        self.assertEqual(fun1(3, 2), 5)
        self.assertEqual(fun1(-1, 1), 0)

    def test_fun2(self):
        self.assertEqual(fun2(5, 3), 2)
        self.assertEqual(fun2(0, 5), -5)

    def test_fun3(self):
        self.assertEqual(fun3(4, 3), 12)
        self.assertEqual(fun3(-2, 3), -6)

    def test_fun4(self):
        self.assertEqual(fun4(3, 2), 12)

if __name__ == '__main__':
    unittest.main()
