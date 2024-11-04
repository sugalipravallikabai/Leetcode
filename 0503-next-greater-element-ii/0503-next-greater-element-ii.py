class Solution:
    def nextGreaterElements(self, n: List[int]) -> List[int]:
        m = len(n)
        st = []
        ans = [-1]*m
        for i in range(2*m-1,-1,-1):
            while st and st[-1] <= n[i%m]:
                st.pop()
            if i < m:
                if st:
                    ans[i] = st[-1]
            st.append(n[i%m])
        return ans