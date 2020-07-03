ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n, m = nm()

aa = nl()

mx = sum(aa)/(4*m)

a = sorted(aa)[::-1]


for i in range(m):
  if a[i] < mx:
    print('No')
    exit()
print('Yes')

