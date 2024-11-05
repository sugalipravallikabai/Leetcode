class Solution:
    def carFleet(self, t: int, pos: List[int], s: List[int]) -> int:
        p = []
        
        for i in range(len(pos)):
            p.append([pos[i],s[i]])
        
        p = sorted(p)[::-1]
        
        st = []
        for i,v in p:
            val = (t-i)/v
            st.append(val)
            if len(st) >= 2 and st[-1] <= st[-2]:
                st.pop()
            
        return len(st)
            