class Solution:
    def maxWidthRamp(self, n: List[int]) -> int:
        st = []
        for i in range(len(n)):
            if not st or n[i] < n[st[-1]]:
                st.append(i)
        m = 0
        for j in range(len(n)-1,-1,-1):
            while st and n[j] >= n[st[-1]]:
                i = st.pop()
                m = max(m,j-i)
        return m