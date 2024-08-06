class Solution:
    def longestAlternatingSubarray(self, a: List[int], t: int) -> int:
        n = len(a)
        ans = 0
        c = 0  
        st = -1  

        for i in range(n):
            
            if a[i] > t:
                st = -1
                c = 0
            elif a[i] % 2 == 0 and st == -1:
                c = 1
                st = i
            elif st > -1:
                if a[i] % 2 !=  a[i-1] % 2:
                    c+=1
                elif a[i] % 2 == 0:
                    st = i
                    c = 1
                else:
                    st = -1
                    c = 0
            ans = max(ans,c)
            
        return ans
                    

