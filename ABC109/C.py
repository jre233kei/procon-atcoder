import heapq
from fractions import gcd
from functools import reduce

ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n, x = nm()
xl = nl()

xl.append(x)

heapq.heapify(xl)


hl = []

last = heapq.heappop(xl)
for i in range(n):
    h = heapq.heappop(xl)
    hl.append(h-last)

print(reduce(gcd,hl))


