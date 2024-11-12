# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        st = []
        if not root:
            return st
        st.append(root)
        while st:
            cur = []
            for i in range(len(st)):
                node = st.pop(0)
                cur.append(node.val)
                if node.left:
                    st.append(node.left)
                if node.right:
                    st.append(node.right)
            ans.append(cur)
        return ans
            