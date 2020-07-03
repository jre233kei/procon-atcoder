ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n,x,y = nm()

dist = [0]*n

for i in range(1,n+1):
  for j in range(i+1,n+1):
    naive = j-i
    cand = naive
    if i<x:
      if x<=j<=y:
        cand = x-i+1+y-j
      elif j>y:
        cand = x-i+1+j-y
    elif x<=i<=y:
      if j<=y:
        cand = i-x+1+y-j
      else:
        cand = i-x+1+j-y
    d = min(naive,cand)
    dist[d]+=1

for i in range(1,n):
  print(dist[i])