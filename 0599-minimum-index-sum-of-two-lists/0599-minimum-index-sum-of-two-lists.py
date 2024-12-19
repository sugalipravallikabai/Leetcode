class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = {}
        for i in range(len(list1)):
            d[list1[i]] = i
        ans = []
        mini = float('inf')
        for i in range(len(list2)):
            if list2[i] in d:
                tol = d[list2[i]]+i
                if mini > tol:
                    ans = [list2[i]]
                    mini = tol
                elif mini == tol:
                    ans.append(list2[i])
        return ans