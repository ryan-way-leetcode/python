# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #base case, node can be its own descedant
        if root.val == p.val or root.val == q.val:
            return root

        #if root is between the two values, it is the solution
        if ( root.val < p.val and root.val > q.val
        or root.val > p.val and root.val < q.val):
            return root

        #root is less than both values, solution lies in right subtree
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)

        raise Exception("Unexpected case")