# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, og : TreeNode, clone : TreeNode, tar: TreeNode) -> TreeNode:
        
        def fun(og,clone,tar):
            if not og or not clone:
                return 0
            # res = 0
            if og == tar:
                return clone
            l = fun(og.left,clone.left,tar)
            if l:
                return l
            r = fun(og.right,clone.right,tar)
            return r
            
            # return res
            
        return fun(og,clone,tar)