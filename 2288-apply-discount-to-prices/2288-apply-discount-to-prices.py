class Solution:
    def discountPrices(self, s : str, discount: int) -> str:
        l = s.split(' ')
        def fun(s):
            return 
        for i in range(len(l)):
            if l[i][0] == '$' and l[i][1:].isnumeric():
                price = int(l[i][1:])
                final = abs(((discount/100)*price)-price)
                l[i] = '$'+ f"{final:.2f}"
        return ' '.join(l)