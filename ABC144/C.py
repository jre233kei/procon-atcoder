ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

import math

n = ni()
nn = n
mn = 10**12
nums = [1]

i=2
while i<=math.ceil(math.sqrt(n)+1):
  if n%i==0:
    nums.append(i)
  i+=1

for num in nums:
  other = nn//num
  mn = min(mn, num+other-2)

print(mn)