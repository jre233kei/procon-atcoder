n, k = map(int, input().split())
h = []
for i in range(n):
    h.append(int(input()))


sh = sorted(h)

min_ = 10**10
for i in range(n-k+1):
    min_ = min(min_,sh[i+k-1]-sh[i])

print(min_)