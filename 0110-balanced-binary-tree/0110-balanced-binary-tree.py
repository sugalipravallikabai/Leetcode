# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def fun(node):
            if not node:
                return 0
            lh = fun(node.left)
            rh = fun(node.right)
            
            if lh == -1 or rh == -1:
                return -1
            if abs(lh-rh) > 1:
                return -1
            return max(lh,rh)+1
        
        return True if fun(root) != -1 else False