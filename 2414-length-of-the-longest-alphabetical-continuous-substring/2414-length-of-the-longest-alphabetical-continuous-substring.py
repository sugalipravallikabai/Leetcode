class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        st = []
        for i in range(len(s)):
            st.append(ord(s[i]))
        cnt = 1
        i = 1
        n = len(st)
        maxi = 1
        while i < n:
            if st[i] == st[i-1]+1:
                cnt += 1
            else:
                cnt = 1
            
            maxi = max(maxi,cnt)
            i+=1
        return maxi