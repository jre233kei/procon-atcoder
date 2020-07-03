ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

import math

n,k=nm()

print(math.floor(math.log(n,k))+1)