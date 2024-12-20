class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n1 = int(a,2)
        n2 = int(b,2)
        return str(bin(n1+n2)).replace('0b','')