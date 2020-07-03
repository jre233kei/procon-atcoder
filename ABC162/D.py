ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n=ni()
s = input()

rs=0
gs=0
bs=0

for i in range(n):
  if s[i]=='R':
    rs+=1
  elif s[i]=='G':
    gs+=1
  else:
    bs+=1

total = rs*gs*bs

for i in range(n):
  for j in range(i+1,n):
    k=j+j-i
    if k<n:
      if s[i]!=s[j] and s[j]!=s[k] and s[i]!=s[k]:
        total-=1

print(total)
