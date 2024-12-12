class Solution:
    def reverseWords(self, s: str) -> str:
        temp = s.split()
        # print(temp)
        string = ' '.join(temp[::-1])
        return string