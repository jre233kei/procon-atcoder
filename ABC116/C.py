n = int(input())
h = list(map(int, input().split()))
h.insert(0, 0)

cnt = 0

for i in range(n):
    cnt += max(h[i + 1] - h[i], 0)
print(cnt)
