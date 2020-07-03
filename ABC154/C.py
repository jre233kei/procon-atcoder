ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n = ni()
a = nl()

s = set()

for ai in a:
  s.add(ai)

if len(s) == n:
  print('YES')
  exit()
print('NO')