class Solution:
    def nextGreaterElement(self, n1: List[int], n2: List[int]) -> List[int]:
        ans = [-1]*len(n1)
        for i in range(len(n1)):
            d = n1[i]
            st = []
            for j in range(len(n2)-1,-1,-1):
                if d == n2[j]:
                    while st and st[-1] <= d:
                        st.pop()
                    if not st:
                        ans[i] = -1
                    else:
                        ans[i] = st[-1]
                        break
                else:
                    st.append(n2[j])
        return ans
        
        