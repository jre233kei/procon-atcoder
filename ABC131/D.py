n = int(input())

a = []
b = []
for i in range(n):
    aa, bb = map(int, input().split())
    a.append(aa)
    b.append(bb)


s = sorted(range(len(b)), key=lambda k: b[k])
fl = 0
time = 0
for si in s:
    time += a[si]
    if time > b[si]:
        fl = 1

if fl == 0:
    print('Yes')
else:
    print('No')