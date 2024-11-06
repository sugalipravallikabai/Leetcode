class Solution:
    def sumSubarrayMins(self, a: List[int]) -> int:
        nse = [len(a)]*len(a)
        st = []
        mod = 10**9+7
        for i in range(len(a)-1,-1,-1):
            while st and a[st[-1]] >= a[i]:
                st.pop()
            if st:
                nse[i] = st[-1]
            st.append(i)
        pse = [-1]*len(a)
        st = []
        for i in range(len(a)):
            while st and a[st[-1]] > a[i]:
                st.pop()
            if st:
                pse[i]=st[-1]
            st.append(i)
        # print(nse,pse)
        tol = 0
        for i in range(len(a)):
            left = nse[i] - i
            right = i -pse[i]
            tol = (tol + (left*right*a[i])%mod)%mod
        
        return tol
            
        