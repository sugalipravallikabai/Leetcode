# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def fun(node):
            if not node:
                return  None
            
            lef = fun(node.left)
            rgt = fun(node.right)
            if lef:
                lef.right = node.right
                node.right = node.left
                node.left = None
            return rgt if rgt else lef if lef else node
            
        
        return fun(root)