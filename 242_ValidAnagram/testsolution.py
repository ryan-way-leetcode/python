import unittest
from solution import Solution

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        s = 'cbaebabacd'
        p = 'abc'

        self.assertEqual(self.s.findAnagrams(s, p), [0, 6])

    def test_example2(self):
        s = 'abab'
        p = 'ab'

        self.assertEqual(self.s.findAnagrams(s, p), [0, 1, 2])