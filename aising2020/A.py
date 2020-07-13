ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

l,r,d=nm()

cnt=0
for i in range(l,r+1):
  if i%d==0:
    cnt+=1

print(cnt)
