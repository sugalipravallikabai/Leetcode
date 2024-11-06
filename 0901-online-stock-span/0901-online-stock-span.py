class StockSpanner:

    def __init__(self):
        self.a = []

    def next(self, price: int) -> int:
        st = self.a
        cnt = 1
        cur_p = price
        while st and st[-1][0] <= cur_p:
            prev_p,prev_span = st.pop()
            cnt += prev_span
            
        st.append([cur_p,cnt])
        
        return cnt


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)