ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n=ni()
a=sorted(nl())[::-1]
 
ans=0

cur=0
now=1
for i in range(n-1):
  ans+=a[cur]
  if now==1:
    now=0
    cur+=1
  elif now==0:
    now=1


print(ans)
