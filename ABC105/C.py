import math

ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n = ni()

k = math.ceil(math.log2(abs(n)))

l = []
a = 0
for i in range(k - 1, 0):
    if i % 2 == 1:
        if (-2) ** i < n:
            n += (-2)**i
    else:
        if (-2) ** i > n:
            n += (-2)**i
