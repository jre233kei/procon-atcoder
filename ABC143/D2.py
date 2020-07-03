import bisect
import heapq

ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n = ni()
l = nl()

l = sorted(l)[::-1]

ans = 0


for a in range(n):
    t = []

    for b in range(a+1,n):
        for c in range(b+1,n):
            t.append(l[b] + l[c])
    y = sorted(t)[::-1]
    print(t)

    bis = bisect.bisect_right(t,a)
    ans += bis

print(ans)