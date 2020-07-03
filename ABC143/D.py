import bisect

ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n = ni()
l = nl()

l = sorted(l)

ans = 0

for a in range(n):
    fl = 0
    A = l[a]
    for b in range(a+1,n):
        B = l[b]

        idx = bisect.bisect_left(l, A+B)
        ans += max(0,idx-b-1)

print(ans)