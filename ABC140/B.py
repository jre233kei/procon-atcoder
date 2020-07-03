n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

sum = 0

last = -99
for i in range(0, n):
    now = a[i]

    sum += b[now - 1]

    if last + 1 == now:
        sum += c[last - 1]
    last = now

print(sum)
