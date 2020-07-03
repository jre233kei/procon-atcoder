ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

x,y = nm()

for i in range(x+1):
  if 2*i+4*(x-i)==y:
    print('Yes')
    exit()

print('No')