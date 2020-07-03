ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

acs = set()
wcs = dict()
wc = 0

n,m = nm()
for i in range(m):
  p,s = input().split()
  if s == 'AC':
    if p not in acs:
      if p in wcs:
        wc+=wcs[p]
    acs.add(p)
  elif p not in acs:
    if p not in wcs:
      wcs[p]=0
    wcs[p]+=1

print(len(acs))
print(wc)