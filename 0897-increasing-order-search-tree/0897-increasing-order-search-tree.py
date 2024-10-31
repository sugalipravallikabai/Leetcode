# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ptr = TreeNode()
        res  = ptr
        def fun(node):
            nonlocal ptr
            if not node:
                return
            fun(node.left)
            ptr.right = TreeNode(node.val)
            ptr = ptr.right
            fun(node.right)
        
        fun(root)
        return res.right
            
        