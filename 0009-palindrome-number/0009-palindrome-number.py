class Solution:
    def isPalindrome(self, x: int) -> bool:
        og = x
        x = abs(x)
        rem = 0
        while x > 0:
            temp = x % 10
            rem = rem*10 + temp
            x = x // 10
        return og == rem