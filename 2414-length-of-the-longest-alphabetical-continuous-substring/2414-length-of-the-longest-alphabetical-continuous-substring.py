class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        if not s:  # Handle edge case for empty string
            return 0
        
        cnt = 1  # Start with 1 to count the first character
        maxi = 1  # Initial max length is at least 1 since every single char is a substring
        
        for i in range(1, len(s)):
            if ord(s[i]) == ord(s[i-1]) + 1:
                cnt += 1
            else:
                cnt = 1  # Reset to 1 when continuity breaks
            
            maxi = max(maxi, cnt)  # Update max length
        
        return maxi
