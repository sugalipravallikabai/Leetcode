# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return []
        width = 0
        que = []
        que.append([root,0])
        while que:
            f,s = 0,0
            mini = que[0][1]
            n = len(que)
            for i in range(n):
                node = que[0][0]
                cur = que[0][1] - mini
                que.pop(0)
                if i == 0: f = cur
                if i == n-1: s = cur
                if node.left:
                    que.append([node.left,(2*cur)+1])
                if node.right:
                    que.append([node.right,(2*cur)+2])
            width = max(width,s-f+1)
        return width
            