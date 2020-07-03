ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n = ni()
x = nl()

mn = 100100100
for p in range(101):
  cnt = 0
  for xi in x:
    cnt += (p-xi)**2
  mn = min(mn, cnt)
print(mn)