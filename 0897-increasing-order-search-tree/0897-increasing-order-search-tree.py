# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dummy  = TreeNode(-1)
        temp = dummy
        cur = root
        while cur:
            if not cur.left:
                temp.right = cur
                cur = cur.right
                temp = temp.right
            else:
                pred = cur.left
                while pred.right and pred.right != cur:
                    pred = pred.right
                if not pred.right:
                    pred.right = cur
                    cur = cur.left
                else:
                    temp.right = cur
                    cur.left = None
                    temp = temp.right
                    cur = cur.right
        return dummy.right
            
        