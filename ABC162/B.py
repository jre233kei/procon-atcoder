ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n = ni()

fa = []

for i in range(10**6+1):
  if i % 3 != 0 and i % 5 !=0:
    fa.append(i)

sum = 0
for i in fa:
  if i <= n:
    sum += i

print(sum)