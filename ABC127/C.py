n, m = map(int, input().split())

maxl = 0
minr = 10 ** 6
for i in range(m):
    l, r = map(int, input().split())
    maxl = max(maxl,l)
    minr = min(minr,r)

if minr < maxl:
    print(0)
else:
    print(minr-maxl+1)