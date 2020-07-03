from math import factorial

import sys

sys.setrecursionlimit(10000)

ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

x,y = nm()

if (x+y)%3!=0:
  print(0)
  exit()

mod = 10**9+7

n = (x+y)//3
a,b = x-n,y-n

fab = factorial(a+b)%mod
fa = factorial(a)%mod
fb = factorial(b)%mod

def power_func(a,b,p):
  """a^b mod p を求める"""
  if b==0: return 1
  if b%2==0:
    d=power_func(a,b//2,p)
    return d*d %p
  if b%2==1:
    return (a*power_func(a,b-1,p))%p

ans = (fab*power_func(fa,mod-2,mod)*power_func(fb,mod-2,mod))%mod


print(ans)