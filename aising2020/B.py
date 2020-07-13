ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n=ni()
a=nl()
cnt=0
for i in range(n):
  if (i+1)%2==1 and a[i]%2==1:
    cnt+=1

print(cnt)
