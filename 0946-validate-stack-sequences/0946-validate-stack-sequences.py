class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st = []
        r = 0
        for i in range(len(pushed)):
            if pushed[i] not in st:
                st.append(pushed[i])
            while st and st[-1] == popped[r]:
                st.pop()
                r+=1
        print(st)
        return len(st) == 0