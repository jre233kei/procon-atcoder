ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

x=nl()
for i in range(5):
  if x[i] == 0:
    print(i+1)