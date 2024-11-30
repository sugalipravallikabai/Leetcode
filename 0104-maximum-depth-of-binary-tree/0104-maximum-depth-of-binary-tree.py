# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def fun(node):
            if not root:
                return 0
            if not node:
                return 0
            lh = fun(node.left)
            rh = fun(node.right)
            
            return 1+max(lh,rh)
        return fun(root)