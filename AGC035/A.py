ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n = ni()
a = nl()

s = 0

for i in range(n):
    s ^= a[i]
if s == 0:
    print('Yes')
else:
    print('No')
