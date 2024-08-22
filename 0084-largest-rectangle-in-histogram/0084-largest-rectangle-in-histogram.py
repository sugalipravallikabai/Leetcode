class Solution:
    def largestRectangleArea(self, a : List[int]) -> int:
        
        st = []
        maxi = 0
        for i in range(len(a)):
            while st and a[st[-1]] > a[i]:
                ele = st.pop()
                nse = i
                if st :
                    pse = st[-1]
                else:
                    pse = -1
                maxi = max(maxi,a[ele]*(nse-pse-1))
            st.append(i)
        while st:
            nse = len(a)
            ele = st.pop()
            if st:
                pse = st[-1]
            else:
                pse = -1
            maxi = max(maxi,a[ele]*(nse-pse-1))
        return maxi