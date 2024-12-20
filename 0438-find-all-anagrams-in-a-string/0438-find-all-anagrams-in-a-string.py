
from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m = len(s), len(p)
        if n < m:
            return []

        p_count = Counter(p)
        s_count = Counter(s[:m])  # Initial window
        ans = []

        # Check the initial window
        if p_count == s_count:
            ans.append(0)

        # Slide the window over `s`
        for i in range(m, n):
            # Include the new character in the window
            s_count[s[i]] += 1
            # Remove the character that's no longer in the window
            s_count[s[i - m]] -= 1

            # If the count of a character becomes zero, remove it from the dictionary
            if s_count[s[i - m]] == 0:
                del s_count[s[i - m]]

            # Compare the current window with `p`
            if s_count == p_count:
                ans.append(i - m + 1)

        return ans
