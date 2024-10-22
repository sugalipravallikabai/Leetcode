# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st = []
        ans = []
        if not root:
            return ans
        st.append(root)
        
        while st:
            node = st.pop()
            ans.append(node.val)
            if node.left:
                st.append(node.left)
            if node.right:
                st.append(node.right)
        ans[:] = ans[::-1]
        return ans
            
            
        