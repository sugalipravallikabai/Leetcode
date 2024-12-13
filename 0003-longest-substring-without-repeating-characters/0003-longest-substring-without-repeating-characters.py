class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = []
        maxi = 0
        for c in s:
            while c in st:
                st.pop(0)
            st.append(c)
            maxi = max(maxi,len(st))
        return maxi
    
            