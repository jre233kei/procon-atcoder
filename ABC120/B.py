import math
a, b, k = map(int, input().split())

cands = []
for i in range(1,int(math.sqrt(a*b)+1)):
    if a % i == 0 and b % i == 0:
        cands.append(i)

print(cands[::-1][k-1])