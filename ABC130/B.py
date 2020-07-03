n, x = map(int, input().split())
l = list(map(int, input().split()))

pos = 0
cnt = 0
for i in range(n):
    pos += l[i]
    if pos > x:
        break
    cnt += 1

print(cnt + 1)
