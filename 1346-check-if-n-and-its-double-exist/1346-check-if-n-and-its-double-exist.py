class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        n = len(arr)
        d = {num : i for i,num in enumerate(arr)}
        for i in range(n):
            val = arr[i]*2
            if val in d and d[val] != i:
                return True
        return False