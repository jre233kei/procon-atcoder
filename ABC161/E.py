ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n,k,c = nm()
s = input()

def valid_work(ss):
  wc = 0
  for i in range(n):
    if ss[i] == True:
      if wc == 0:
        wc = c
        continue
      return False
    wc -= 1
  return True

def calc(ss):
  if len(ss) == n:
    return ss

  last = len(ss)
  if s[last] == 'o':
    cc = []
    c1 = calc(ss+[True])
    c2 = calc(ss+[False])
    for i in range(n):
      if c1[i]==True and c2[i]==True:
        cc.append(True)
      else:
        cc.append(False)
    return cc
  return calc(ss+[False])

ccc = calc([])
for i in range(n):
  if ccc[i] == True:
    print(i+1)






