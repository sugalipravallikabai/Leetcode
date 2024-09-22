class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        l = sorted(range(1,n+1),key=str)
        # print(l)
        return l