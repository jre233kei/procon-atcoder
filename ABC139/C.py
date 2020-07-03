n = int(input())
h = list(map(int, input().split()))

last = 0
maxcnt = 0
cnt = 0

for i in range(n):
    if h[i] > last:
        cnt = 0
    if cnt > maxcnt:
        maxcnt = cnt
    last = h[i]
    cnt += 1
print(maxcnt)

