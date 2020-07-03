ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n,m,k=nm()
a=nl()
b=nl()

aa,bb=[0],[0]
for i in range(n):
  aa.append(a[i]+aa[i])
for i in range(m):
  bb.append(b[i]+bb[i])

ans,j=0,m
for i in range(n+1):
  if aa[i]>k:
    break
  while bb[j]>k-aa[i]:
    j-=1
  ans=max(ans,i+j)
print(ans)