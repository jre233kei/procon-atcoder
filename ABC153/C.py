ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n,k=nm()
h = nl()

sh = sorted(h)[::-1]

if k>=n:
  print(0)
  exit()

print(sum(sh[k:]))