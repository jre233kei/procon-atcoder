ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

import math

MAX=10**6+1

n=ni()
a=nl()

s = [0]*(MAX)

for ai in a:
  if s[ai]!=0:
    s[ai]=2
    continue
  for i in range(ai,MAX,ai):
    s[i]+=1

cnt=0
for ai in a:
  if s[ai]==1:
    cnt+=1

print(cnt)