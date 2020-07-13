ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

import math

n = ni()
if n%1000==0:
  print(0)
else:
  print(1000-n%1000)
