# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def fun(node,tol,low,high):
            if not node:
                return 0
            tol = 0
            
            if node.val >= low and node.val <= high:
                tol += node.val
            tol += fun(node.left,tol,low,high)
            tol += fun(node.right,tol,low,high)
            return tol
        
        return fun(root,0,low,high)