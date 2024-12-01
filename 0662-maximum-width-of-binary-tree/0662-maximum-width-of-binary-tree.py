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
            return 0
        width = 0
        que = deque()
        que.append([root,0])
        while que:
            mini = que[0][1]
            f,s = 0,0
            n = len(que)
            for i in range(n):
                value = que.popleft()
                curid = value[1]-mini
                node = value[0]
                if i == 0:
                    f = curid
                if i == n-1:
                    s = curid
                if node.left:
                    que.append([node.left,(2*curid)+1])
                if node.right:
                    que.append([node.right,(2*curid)+2])
            width = max(width,s-f+1)
        return width
            
            
            
            
            
            
            
            
            
            