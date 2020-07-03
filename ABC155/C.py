ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n = ni()
s = dict()

for i in range(n):
  si = input()
  if si in s:
    s[si]+=1
  else:
    s[si]=1

ss = sorted([(_[1], _[0]) for _ in s.items()])[::-1]

mx = ss[0][0]

ssr = []
for ssi in ss:
  if ssi[0] == mx:
    ssr.append(ssi[1])
sss = sorted(ssr)

for sssi in sss:
  print(sssi)