ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n,k = nm()
r,s,p=nm()
t = [_ for _ in input()]
tt=[]
for ti in t:
  if ti == 'r':
    tt.append(0)
  elif ti == 's':
    tt.append(1)
  else:
    tt.append(2)

score=dict()
res=0
for i in range(k):
  last=False
  for j in range(i,n,k):
    if j>=k and tt[j-k]==tt[j] and last:
      last=False
    else:
      if tt[j]==0:
        res+=p
      elif tt[j]==1:
        res+=r
      else:
        res+=s
      
      last=True
print(res)
    