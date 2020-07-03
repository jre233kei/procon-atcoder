ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n = ni()

for i in range(10):
  for j in range(10):
    if i*j == n:
      print('Yes')
      exit()
print('No')