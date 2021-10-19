import unittest
from solution import Solution, TreeNode

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        test = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))

        self.assertEqual(set(self.s.binaryTreePaths(test)), 
        set(["1->2->5", "1->3"]))