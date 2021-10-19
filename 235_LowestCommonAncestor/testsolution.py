import unittest
from solution import Solution, TreeNode

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()
        self.tree = TreeNode(6)
        self.tree.left = TreeNode(2)
        self.tree.right = TreeNode(8)

        self.tree.left.left = TreeNode(0)
        self.tree.left.right = TreeNode(4)

        self.tree.left.right.left = TreeNode(3)
        self.tree.left.right.right = TreeNode(5)

        self.tree.right.left = TreeNode(7)
        self.tree.right.right = TreeNode(9)

    def test_example1(self):
        exp = TreeNode(6)

        act = self.s.lowestCommonAncestor(self.tree, TreeNode(2), TreeNode(8))

        self.assertEqual(exp.val, act.val)

    def test_example2(self):
        exp = TreeNode(2)

        act = self.s.lowestCommonAncestor(self.tree, TreeNode(2), TreeNode(2))

        self.assertEqual(exp.val, act.val)