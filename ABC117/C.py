n, m = map(int, input().split())
x = sorted(list(map(int, input().split())))

koma_dist = []

for i in range(m - 1):
    koma_dist.append(x[i + 1] - x[i])

if n<m:
    print(sum(sorted(koma_dist)[:m-n]))
else:
    print(0)
