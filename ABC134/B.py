import math
n, d = map(int, input().split())

if n % (2 * d + 1) == 0:
    print(math.floor(n / (2 * d + 1)))
else:
    print(math.floor(n / (2 * d + 1)) + 1)
