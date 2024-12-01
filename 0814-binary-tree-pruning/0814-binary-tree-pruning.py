# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        def fun(node):
            if not node:
                return False
            lh = fun(node.left)
            rh = fun(node.right)
            if not lh:
                node.left = None
            if not rh:
                node.right = None
            return node.val == 1 or lh or rh
        
        return root if fun(root) else None