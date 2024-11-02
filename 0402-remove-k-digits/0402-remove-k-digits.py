class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return '0'
        st = []
        for i in num:
            while st and k > 0 and st[-1] > int(i):
                st.pop()
                k -= 1
            st.append(int(i))
        while k > 0 :
            st.pop()
            k-=1    
        ans = ''.join(map(str, st)).lstrip('0')
        
        return ans if ans else '0'
            