ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

INF = 10**10

h,n = nm()

dp = [INF] * (h+1)

dp[0] = 0

for i in range(n):
  a,b = nm()

  for j in range(h):
    nj = min(j+a,h) 
    dp[nj]=min(dp[nj],dp[j]+b) # ダメージがj+aの時のコスト

print(dp[h])
