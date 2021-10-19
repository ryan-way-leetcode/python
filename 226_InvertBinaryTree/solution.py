# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __eq__(self, node):
        if node is None: return False
        return (self.val == node.val 
            and self.right == node.right 
            and self.left == node.left)


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is not None:
            root.left = self.invertTree(root.left)
            root.right = self.invertTree(root.right)

            root.left, root.right = root.right, root.left
        
        return root

