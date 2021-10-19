import unittest
from solution import Solution

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        test = 6
        
        self.assertTrue(self.s.isUgly(test))

    def test_example2(self):
        test = 8

        self.assertTrue(self.s.isUgly(test))

    def test_example3(self):
        test = 14

        self.assertFalse(self.s.isUgly(test))

    def test_user1(self):
        test = -8

        self.assertFalse(self.s.isUgly(test))

    def test_user2(self):
        test = 1

        self.assertTrue(self.s.isUgly(test))

    def test_failed1(self):
        test = 0

        self.assertFalse(self.s.isUgly(test))