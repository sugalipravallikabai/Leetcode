class Solution:
    def removeKdigits(self, n : str, k: int) -> str:
        if len(n) == k:
            return '0'
        st = []
        for i in range(len(n)):
            while st and k > 0 and int(st[-1]) > int(n[i]) :
                st.pop()
                k -= 1
            st.append(n[i])
        while k != 0:
            st.pop()
            k -= 1
        res =  ''.join(st).lstrip('0')
        return res if res else '0'