from collections import deque

ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n,m = nm()

p = [[] for _ in range(n)]

for i in range(m):
  a,b = nm()
  p[a-1].append(b-1)
  p[b-1].append(a-1)

visited = [False]*n

visited[0]=True

q = deque()
q.append(0)

ans = [0]*n

while len(q) > 0:
  num = q.popleft()
  for i in p[num]:
    if visited[i]:
      continue
    ans[i]=num+1
    visited[i]=True
    q.append(i)

if len(visited)==n:
  print('Yes')
  for i in range(1,len(ans)):
    print(ans[i])
else:
  print('No')