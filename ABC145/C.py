import math

ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n = ni()

x = []
y = []

for i in range(n):
  a,b = nm()
  x.append(a)
  y.append(b)

cnt = 0

def dist(xi,yi,xj,yj):
  return math.sqrt((xi-xj)**2+(yi-yj)**2)

def search(route):
  global cnt
  s = 0
  if len(route) == n:
    cnt += 1
    for i in range(n-1):
      s += dist(x[route[i]],y[route[i]],x[route[i+1]],y[route[i+1]])
    return s
  for i in range(n):
    if i not in route:
      s+=search(route+[i])
  return s

ans = search([])/cnt
print(ans)