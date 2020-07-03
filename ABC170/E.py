ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

import math

n=ni()
a=sorted(nl())

sa = []

ans=0

last=-1
cnt=0
for i in range(n):
  if a[i]!=last:
    cnt=0
    last=a[i]
  else:
    cnt+=1
  if cnt <= 2:
    sa.append(a[i])


l =len(sa)


for i in range(l):
  for j in range(l):
    if i==j:
      continue
    if sa[i]%sa[j]==0:
      break
  if j==n-1:
    ans+=1

print(ans)


  

