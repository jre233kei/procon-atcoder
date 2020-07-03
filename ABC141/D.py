import heapq
import math

class Heapq:
    def __init__(self, arr, desc=False):
        if desc:
            arr = [-a for a in arr]
        self.sign = -1 if desc else 1
        self.hq = arr
        heapq.heapify(self.hq)

    def pop(self):
        return heapq.heappop(self.hq) * self.sign

    def push(self, a):
        heapq.heappush(self.hq, a * self.sign)

    def top(self):
        return self.hq[0] * self.sign


n, m = map(int,input().split())
a = list(map(int, input().split()))

q = Heapq(a, desc=True)

for i in range(m):
    qi = q.pop()
    q.push(math.floor(qi/2))

ans = 0

for i in range(n):
    ans += q.pop()

print(ans)