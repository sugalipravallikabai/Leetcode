# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def fun(node):
            if not node:
                return True
            child = 0
            if node.left:
                child += node.left.val
            if node.right:
                child += node.right.val
            if node.left or node.right:
                if child != node.val:
                    return False
            return fun(node.left) and fun(node.right)
        
        return fun(root)