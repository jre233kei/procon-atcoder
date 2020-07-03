ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n = ni()

d = nl()

ans = 0

for i in range(n):
    for j in range(i+1,n):
        ans += d[i] * d[j]

print(ans)