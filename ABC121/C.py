n, m = map(int, input().split())
a = []
b = []

ans = 0

for i in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)

sai = sorted(range(len(a)), key=lambda k: a[k])

for i in range(n):
    bsai = min(m,b[sai[i]])
    m -= bsai
    ans += a[sai[i]]*bsai


print(ans)