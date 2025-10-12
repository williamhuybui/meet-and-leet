from collections import deque

class RecentCounter:
    def __init__(self):
        self.request = deque()

    def ping(self, t: int) -> int:
        self.request.append(t)
        while len(self.request) > 0 and t - self.request[0] > 3000:
            self.request.popleft()
        return len(self.request)
            
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)