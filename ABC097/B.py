ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

x = ni()

num = 1

for i in range(100):
  for j in range(2,10):
    if i**j <= x:
      num = max(num,i**j)

print(num)