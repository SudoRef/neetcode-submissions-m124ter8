class StockSpanner:

    def __init__(self):
        self.queue = deque()
        self.stack = []

    def next(self, price: int) -> int:
        cnt = 1
        while self.stack and price >= self.stack[-1]:
            self.queue.append(self.stack.pop())
            cnt+=1
        while self.queue:
            self.stack.append(self.queue.popleft())
        self.stack.append(price)
        return cnt


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)