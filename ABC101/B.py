ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n = ni()
sn = sum([int(i) for i in str(n)])

if n%sn==0:
  print('Yes')
else:
  print('No')