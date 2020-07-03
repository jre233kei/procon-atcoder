import math

ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

a, b, x = nm()


for i in range(1000000000):
  n = min(1000000000, (x - b * i) // a)
  if n <= 0:
    print(0)
    break
  cost = a * n + b * (math.floor(math.log10(n)) + 1)
  if cost > x:
    continue
  if cost == x:
    print(n)
    break
  print(n)
  break
