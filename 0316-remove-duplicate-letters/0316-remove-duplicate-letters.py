class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        st = []
        seen = set()
        d = {c:i for i,c in enumerate(s)}
        for i,c in enumerate(s):
            if c not in seen:
                
                while st and st[-1] > c and i < d[st[-1]]:
                    
                    seen.discard(st.pop())
                
                st.append(c)
                seen.add(c)
        return ''.join(st)