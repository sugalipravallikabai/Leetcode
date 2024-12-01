# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        def fun(node,level):
            if not node:
                return 
            if len(ans) == level:
                ans.append(node.val)
            fun(node.right,level+1)
            fun(node.left,level+1)
        fun(root,0)
        return ans