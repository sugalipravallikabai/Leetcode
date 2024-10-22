class Solution:
    def nextGreaterElement(self, n1: List[int], n2: List[int]) -> List[int]:
        d = {}
        st = []
        for i in reversed(n2):
            
            while st and st[-1] < i:
                st.pop()
            if st:
                d[i] = st[-1]
            else:
                d[i] = -1
            
            st.append(i)
            
        return [d[num] for num in n1]
        
        