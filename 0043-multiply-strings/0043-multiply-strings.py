class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = 0
        n2 = 0
        print(int('233'))
        for num in num1:
            n1 = n1*10+int(num)
        
        return str(int(num1)*int(num2))