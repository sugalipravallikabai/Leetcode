class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        l = list(s.split(" "))
        # t = ""
        return " ".join(l[:k])
        