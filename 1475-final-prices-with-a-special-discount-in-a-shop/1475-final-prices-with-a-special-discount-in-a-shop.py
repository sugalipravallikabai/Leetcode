class Solution:
    def finalPrices(self, p : List[int]) -> List[int]:
        res = p[:]
        st = []
        for i in range(len(p)):
            while st and p[st[-1]] >= p[i]:
                j = st.pop()
                res[j] -= p[i]
            st.append(i)
        return res
        