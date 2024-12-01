# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        d = defaultdict(list)
        que = deque()
        que.append([root,0,0])
        while que:
            value = que.popleft()
            node = value[0]
            line = value[1]
            level = value[2]
            d[line].append([level,node.val])
            if node.left:
                que.append([node.left,line-1,level+1])
            if node.right:
                que.append([node.right,line+1,level+1])
        res = []
        for key in sorted(d):
            col = sorted(d[key] , key = lambda x: (x[0],x[1]))
            res.append([val for _,val in col])
        return res
        