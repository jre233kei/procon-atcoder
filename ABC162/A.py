ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n = ni()

for s in str(n):
  i = int(s)
  if i == 7:
    print('Yes')
    exit()

print('No')