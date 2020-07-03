ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

l,r = nm()

MOD = 2019

ans = 10**9
for i in range(l,min(r,l+2019)+1):
  for j in range(i+1,min(r,i+MOD)+1):
    ans=min(ans,((i%MOD)*(j%MOD))%MOD)

print(ans)
