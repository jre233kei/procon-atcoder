ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

import math


n = ni()

nums = [1]*(n+1)

for i in range(2,n+1):
  for j in range(i,n+1,i):
    nums[j]+=1

# print(nums)
cnt=0
for i in range(n+1):
  cnt+=nums[i]*i

print(cnt)