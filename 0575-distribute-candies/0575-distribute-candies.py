class Solution:
    def distributeCandies(self, c : List[int]) -> int:
        n = len(c)
        candy = set(c)
        # print(candy)
        if len(candy) < n//2:
            return len(candy)
        return n//2