ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

import math

d=ni()

x=0
y=1
cnt=0
dd=0
while True:
  cnt+=1
  dd=(dd+d)%360
  r = math.radians(dd)
  x += math.sin(r)
  y += math.cos(r)

  # print("{}, {}".format(x,y))

  if abs(x)<10**(-10) and abs(y)<10**(-10):
    break
print(cnt+1)



