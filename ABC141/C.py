n, k, q = map(int, input().split())

p = [k] * n

for i in range(q):
    a = int(input()) - 1
    p[a] += 1

for i in range(n):
    if p[i] <= q:
        print('No')
    else:
        print('Yes')