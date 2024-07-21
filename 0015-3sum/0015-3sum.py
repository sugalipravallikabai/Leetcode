class Solution:
    def threeSum(self, n: List[int]) -> List[List[int]]:
        n.sort()
        k=set()
        for i in range(len(n)):
            l=i+1
            r=len(n)-1
            while l<r:
                if n[i]+n[l]+n[r] == 0:
                    k.add((n[i],n[l],n[r]))
                    l+=1
                    r-=1
                elif n[i]+n[l]+n[r] < 0:
                    l+=1
                else:
                    r-=1
        return list(k)