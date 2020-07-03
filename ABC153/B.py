ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

h,n = nm()
a = nl()

if h<=sum(a):
  print('Yes')
  exit()
print('No')