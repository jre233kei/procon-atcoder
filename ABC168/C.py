ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

import math

a,b,h,m=nm()

dh = (h+m/60)/12*360
dm = m/60*360

theta = abs(dh-dm)
if theta >= 180:
  theta = 360-theta

ans = a**2+b**2-2*a*b*math.cos(math.radians(theta))

print(math.sqrt(ans))