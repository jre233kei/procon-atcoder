ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n = ni()

table = [[] for _ in range(n)]

for i in range(n):
  for j in range(n):
    table[i].append(-1)

for i in range(n):
  a = ni()
  for j in range(a):
    x, y = nm()
    if y == 1:
      table[i][x-1] = 1
    else:
      table[i][x-1] = 0

ans=0

for i in range(2**n):
  ok = True
  num = 0
  for j in range(n):
    if not 1 & (i>>j):
      continue
    num+=1
    for k in range(n):
      if table[j][k] ==-1:
        continue
      if table[k][j] == 0:
        ok = False
    if ok:
      ans = max(ans,num)

print(ans)





