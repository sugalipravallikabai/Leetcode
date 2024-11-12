class Solution:
    def summaryRanges(self, n : List[int]) -> List[str]:
        if not n:
            return n
        m = n[0]
        k = m+1
        st = []
        for i in range(1,len(n)):
            if k == n[i]:
                k += 1
            else:
                if m == n[i-1]:
                    st.append(str(m))
                else:
                    st.append(str(m)+'->'+str(n[i-1]))
                m = n[i]
                k = m+1
        if m == n[-1]:
            st.append(str(m))
        else:
            st.append(str(m)+'->'+str(n[-1]))
        return st