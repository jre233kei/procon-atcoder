ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

a,b = map(float, input().split())

import math

bint = round(b*100)
aint = round(a)
print(aint*bint//100)