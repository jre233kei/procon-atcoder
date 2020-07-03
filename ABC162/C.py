import math
from functools import reduce

ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

k=ni()

ans = 0
for a in range(1,k+1):
  for b in range(1,k+1):
    for c in range(1,k+1):
      arr = [a,b,c]
      r = reduce(math.gcd, arr)
      ans+=r

print(ans)