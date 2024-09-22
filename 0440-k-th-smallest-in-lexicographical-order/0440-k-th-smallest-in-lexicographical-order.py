class Solution:
    def findKthNumber(self, n: int, k: int) -> int:

        # l = sorted(range(1,n+1),key=str)
        # return l[k-1]

        def count_steps(cur,n):
            steps = 0
            f = cur
            l = cur

            while f <= n:
                steps += min(l,n)-f+1
                f *= 10
                l = l*10+9
            return steps

        cur = 1
        k -= 1

        while k > 0:
            steps = count_steps(cur,n)
            if steps <= k:
                cur += 1
                k -= steps
            else:
                cur *= 10
                k -= 1
        return cur

        