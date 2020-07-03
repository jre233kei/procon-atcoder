ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

MX = 10**18
n=ni()
a = sorted(nl())



num = 1
for i in range(n):
  num*=a[i]
  if num > MX:
    print(-1)
    exit()
print(num)