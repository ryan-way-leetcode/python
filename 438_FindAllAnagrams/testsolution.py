import unittest
from solution import Solution

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        s = 'anagram'
        t = 'nagaram'

        self.assertTrue(self.s.isAnagram(s, t))

    def test_example2(self):
        s = 'rat'
        t = 'car'

        self.assertFalse(self.s.isAnagram(s, t))