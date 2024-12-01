# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        que = []
        que.append(root)
        flag = 0
        while que:
            cur = []
            for i in range(len(que)):
                node = que.pop(0)
                cur.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            if flag == 0:
                ans.append(cur)
                flag = 1
            else:
                cur.reverse()
                ans.append(cur)
                flag = 0
        return ans
            