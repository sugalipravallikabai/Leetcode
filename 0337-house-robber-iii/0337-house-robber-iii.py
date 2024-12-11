# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def fun(node):
            if not node:
                return [0,0]
            lh = fun(node.left)
            rh = fun(node.right)
            rob = node.val + lh[1]+rh[1]
            
            notrob = max(lh)+max(rh)
            return [rob,notrob]
        
        return max(fun(root))
    
            
            