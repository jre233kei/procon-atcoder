import math
n = int(input())
ma = 10**16
ind = 0
for i in range(5):
    ai = int(input())
    if ma >= ai:
        ind = i
        ma = ai
print(math.ceil(n/ma)+4)
