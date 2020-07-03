import math

ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

a,b,x = nm()

if x<(a**2)*b/2:
  ans = math.degrees(math.atan(2*((a**2)*b-x)/(a**2)))
else:
  ans = 90 - math.degrees(math.atan(2*x/a/b))
print(ans)