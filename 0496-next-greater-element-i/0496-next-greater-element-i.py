class Solution:
    def nextGreaterElement(self, n1: List[int], n2: List[int]) -> List[int]:
        res = [0]*len(n1)
        
        for i in range(len(n1)):
            t1 = n1[i]
            st = []
            for j in range(len(n2)-1,-1,-1):
                if t1 == n2[j]:
                    while st and st[-1] <= t1:
                        st.pop()
                    if not st:
                        res[i] = -1
                    else:
                        res[i]=st[-1]
                        break
                else:
                    st.append(n2[j])
        return res