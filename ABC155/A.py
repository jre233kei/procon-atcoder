ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

a = sorted(nl())

if a[0]==a[1] and a[1]!=a[2]:
  print("Yes")
elif a[0]!=a[1] and a[1]==a[2]:
  print('Yes')
else:
  print('No')
