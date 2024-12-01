# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxi = [0]
        def fun(node):
            if not node:
                return 0
            lh = fun(node.left)
            rh = fun(node.right)
            
            maxi[0] = max(maxi[0],lh+rh)
            
            return max(lh,rh)+1
        
        fun(root)
        return maxi[0]
    
    
    
    
    
    
    
    
    