ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))
import copy

h,w,k=nm()

field = []
for y in range(h):
  field.append([_ for _ in input()])

ans=0

s = set()

for yi in range(2**h):
  f1 = copy.deepcopy(field)
  for yj in range(h):
    if ((yi >> yj) & 1):
      f1[yj] = ['*']*w
    for xi in range(2**w):
      f2= copy.deepcopy(f1)
      for xj in range(w):
        if((xi >> xj) & 1):
          for y in range(h):
            f2[y][xj] = '*'
      
      cnt=0
      for y in range(h):
        for x in range(w):
          if f2[y][x] == '#':
            cnt+=1

      if cnt==k:
        ans+=1
        s.add(str(f2))
# print(ans)
print(len(s))
