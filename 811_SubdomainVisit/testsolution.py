import unittest
from solution import Solution

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        cpdomains = ["9001 discuss.leetcode.com"]

        self.assertEqual(set(self.s.subdomainVisits(cpdomains)), 
        set(["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]))

    def test_example2(self):
        cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]

        self.assertEqual(set(self.s.subdomainVisits(cpdomains)), 
        set(["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]))