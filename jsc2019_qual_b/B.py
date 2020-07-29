ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

import copy

mod = 10**9+7

n,k = nm()
a=nl()

p=0

aa = copy.deepcopy(a)
b1 = copy.deepcopy(a)
b2 = copy.deepcopy(a)

for i in range(n*k):
  for j in range(n*k):
    if(b[i]>b[j]):
      b[i],b[j] = b[j], b[i]
      ans+=1
print(ans%mod)
