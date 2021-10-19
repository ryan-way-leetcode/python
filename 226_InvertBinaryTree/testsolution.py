import unittest
from solution import Solution, TreeNode

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_empty(self):
        exp = None
        act = self.s.invertTree(None)

        self.assertEqual(act, exp)

    def test_one(self):
        exp = TreeNode(4, TreeNode(7), TreeNode(2))
        test = TreeNode(4, TreeNode(2), TreeNode(7))

        act = self.s.invertTree(test)

        self.assertEqual(act, exp)

    def test_multipush(self):
        pass