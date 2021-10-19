# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root):
        if root is None:
            return []
        
        results = ( self.binaryTreePaths(root.left) 
                + self.binaryTreePaths(root.right))

        return ([str(root.val)] if len(results) == 0 
            else [str(root.val)+"->"+i for i in results])