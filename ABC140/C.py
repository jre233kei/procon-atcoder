n = int(input())
b = list(map(int, input().split()))

last = 10 ** 6
sum = 0
for i in range(0, n - 1):
    if b[i] < last:
        sum += b[i]
    else:
        sum += last
    last = b[i]

sum += b[n-2]

print(sum)
