class Solution:
    def productExceptSelf(self, n : List[int]) -> List[int]:
        st = [0] * len(n)
        tol = 1
        cnt = 0
        for i in range(len(n)):
            if n[i] != 0:
                tol *= n[i]
            else:
                cnt += 1
        for i in range(len(n)):
            if cnt > 1:
                st[i] = 0
            elif cnt == 1:
                st[i] = tol if n[i] == 0 else 0
            else:
                st[i] = tol // n[i]
        return st