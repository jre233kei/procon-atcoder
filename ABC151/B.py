ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n,k,m = nm()

a = nl()
ans = max(0,m*n-sum(a))

if ans>k:
  print(-1)
  exit()
print(ans)