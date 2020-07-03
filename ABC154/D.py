ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n,k = nm()
p = nl()

def exp(num):
  ret = (1+num)/2
  return ret

mx=0

pp = list(map(exp,p))
pd = [0]*(n+1)



for i in range(1,n+1):
  pd[i] = pd[i-1] + pp[i-1]




for i in range(n-k+1):
  mx = max(pd[i+k]-pd[i],mx)

print(mx)