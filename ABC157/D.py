ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n,m,k=nm()

fr=[[] for _ in range(n)]
bl=[[] for _ in range(n)]


for i in range(m):
  a,b=nm()
  fr[a-1].append(b-1)
  fr[b-1].append(a-1)
for i in range(k):
  c,d=nm()
  bl[c-1].append(d-1)
  bl[d-1].append(c-1)

color=0
colors=[-1]*n

def coloring(num,visited):
  global colors
  for e in fr[num]
  

for i in range(n):
  coloring(i,set())


