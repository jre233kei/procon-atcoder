ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n, m = nm()

dp = [[] for j in range(n)]

keys = []
for i in range(m):
    a, b = nm()
    c = nl()

    keys.append([ci -1 for ci in c])
    for j in range(b):
        dp[c[j] - 1].append((a, i))

for d in dp:
    d.sort()


for i in range(n):
    if len(dp[i]) == 0:
        print(-1)
        exit()

got_keys = set()
pos = [0] * n

ans = 0

while True:
    min_cost = 10 ** 6
    mc_ind = -1

    if len(got_keys) == n:
        break
    for i in range(n):
        if i in got_keys:
            continue
        c = dp[i][pos[i]][0]
        key = dp[i][pos[i]][1]
        if min(c, min_cost) == c:
            min_cost = c
            mc_ind = i
        got_keys |= set(keys[key])
        ans += c

print(ans)
