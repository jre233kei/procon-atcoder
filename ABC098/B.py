ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n=ni()
s=[_ for _ in input()]


mx=0

for i in range(n):
  sr =s[:i]
  sl = s[i:]
  r=set(sr)
  l=set(sl)

  nn=len(r & l)
  mx = max(nn,mx)

print(mx)

