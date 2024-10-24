"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        def fun(root):
            if not root:
                return []
            for c in root.children:
                fun(c)
            ans.append(root.val)
            return ans
        return fun(root)