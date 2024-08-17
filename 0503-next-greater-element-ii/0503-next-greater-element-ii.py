class Solution:
    def nextGreaterElements(self, n : List[int]) -> List[int]:
        st = []
        res = [0]*len(n)
        
        for i in range(2*len(n)-1,-1,-1):
            while st and st[-1] <= n[i % len(n)]:
                st.pop()
            if not st and i < len(n):
                res[i] = -1
            else:
                if i < len(n):
                    res[i] = st[-1]
            st.append(n[i % len(n)])
        
        return res
                