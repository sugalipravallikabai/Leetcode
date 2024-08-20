class Solution:
    def subArrayRanges(self, a : List[int]) -> int:
        
        def nse_fun(a):
            n = len(a)
            st = []
            nse = [0]*n
            for i in range(n-1,-1,-1):
                while st and a[st[-1]] >= a[i]:
                    st.pop()
                if not st:
                    nse[i] = n
                else:
                    nse[i] = st[-1]
                st.append(i)
            return nse
        def pse_fun(a):
            n = len(a)
            st = []
            pse = [0]*n
            for i in range(n):
                while st and a[st[-1]] > a[i]:
                    st.pop()
                if not st:
                    pse[i] = -1
                else:
                    pse[i] = st[-1]
                st.append(i)
            return pse
        def nge_fun(a):
            n = len(a)
            st = []
            nge = [0]*n
            for i in range(n-1,-1,-1):
                while st and a[st[-1]] <= a[i]:
                    st.pop()
                if not st:
                    nge[i] = n
                else:
                    nge[i] = st[-1]
                st.append(i)
            return nge
        def pge_fun(a):
            n = len(a)
            st = []
            pge = [0]*n
            for i in range(n):
                while st and a[st[-1]] < a[i]:
                    st.pop()
                if not st:
                    pge[i] = -1
                else:
                    pge[i] = st[-1]
                st.append(i)
            return pge
        
        n = len(a)
        nse = nse_fun(a)
        pse = pse_fun(a)
        nge = nge_fun(a)
        pge = pge_fun(a)
        tol = 0
        
        for i in range(n):
            
            maxi = (i-pge[i]) * (nge[i]-i) * a[i]
            
            mini = (i-pse[i]) * (nse[i]-i) * a[i]
            
            tol += maxi - mini
        
        return tol
            
        
        
        
        
        
            