class Solution:
    def sumSubarrayMins(self, a : List[int]) -> int:
        
        mod = 10**9+7
        def fun1(a):
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
        def fun2(a):
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
        
        tol = 0
        nse = fun1(a)
        pse = fun2(a)
        for i in range(len(a)):
            left = i-pse[i]
            right = nse[i]-i
            tol = (tol+((left*right*a[i]) % mod)) % mod
        return tol
            
            
        
        
        
        
        
        
        
        
        
        
        