ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n = ni()
a = nl()

s = []

for i in range(n):
  s.append(a[i]-i-1)

avg = sorted(s)[n//2]

dir = 1

last = 0

def getErr(num):
  err = 0
  for i in range(n):
    err += abs(s[i] - num)
  return err

mn = 10**10
for i in range(avg-1000,avg+1000):
  mn = min(mn, getErr(i))

print(mn)
