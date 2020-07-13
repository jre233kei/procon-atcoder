ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

import copy

n=ni()
x=[_ for _ in input()]

def popcount(nn):
  ans=0
  while nn>0:
    if nn%2==1:
      ans+=1
    nn>>=1
  return ans

pc = dict()


def f(nn):
  ans=0
  while nn>0:
    ans+=1
    ppc=1
    if nn in pc:
      ppc = pc[nn]
    else:
      ppc = popcount(nn)
      pc[nn] = ppc
    nn=nn%ppc
  return ans

for i in range(n):
  num = int(''.join(x),2)
  if x[i]=='1':
    num -= 2**(n-i-1)
  else:
    num += 2**(n-i-1)
  # print(num)
  print(f(num))
