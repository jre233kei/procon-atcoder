import math

n, k = map(int, input().split())
ans = 0
for i in range(1, n + 1):
    ans += 1 / n * min((1 / 2) ** math.ceil(math.log2(k / i)), 1)

print(ans)
