ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n = ni()

g = [[] for _ in range(n)]

for i in range(n-1):
  a, b = nm()
  g[a].append((a,b))

colors = [[] for _ in range(n+1)]
childcolors = [[] for _ in range(n+1)]
maxc = 0

for i in range(1, n):

  for j in range(len(g[i])):
    num = 1
    while True:
      if num not in colors[g[i][j][0]] and num not in childcolors[g[i][j][0]]:
        childcolors[g[i][j][0]].append(num)
        colors[g[i][j][1]].append(num)
        maxc = max(maxc, num)
        break
      num += 1

# print(childcolors)
# print(colors)

print(maxc)
for c in colors:
  if len(c) > 0:
    print(c[0])


