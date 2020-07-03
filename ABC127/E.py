ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n, m = nm()

a = sorted(nl())

pos = 0

changer = []

for i in range(m):
    b, c = nm()
    changer.append((c, b))

changer = sorted(changer)[::-1]


for i in range(m):

    c = changer[i]
    for j in range(c[1]):
        while pos < n:
            if a[pos] < c[0]:
                a[pos] = c[0]
                break
            pos += 1
    if pos >= n:
        break

print(sum(a))
