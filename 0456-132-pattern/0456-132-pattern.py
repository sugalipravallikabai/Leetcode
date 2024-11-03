class Solution:
    def find132pattern(self, n: List[int]) -> bool:
        st = []
        s3 = float('-inf')
        for i in reversed(n):
            if i < s3:
                return True
            while st and st[-1] < i:
                s3 = st.pop()
            st.append(i)
        return False