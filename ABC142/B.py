ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n, k = nm()

h = nl()

cnt = 0

for i in range(n):
    if h[i] >= k:
        cnt += 1

print(cnt)