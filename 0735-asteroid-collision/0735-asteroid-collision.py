class Solution:
    def asteroidCollision(self, a : List[int]) -> List[int]:
        
        st = []
        for i in range(len(a)):
            if a[i] > 0:
                st.append(a[i])
            else:
                while st and st[-1] > 0 and st[-1] < abs(a[i]):
                    st.pop()
                if st and st[-1] == abs(a[i]):
                    st.pop()
                elif not st or st[-1] < 0:
                    st.append(a[i])
        return st
                