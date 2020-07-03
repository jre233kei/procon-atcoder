ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n=ni()
p=nl()
q=nl()

cnt=0

pnum=0
qnum=0

def comb(nums):
  global cnt
  global pnum
  global qnum
  if len(nums)==n:
    cnt+=1
    if nums == p:
      pnum = cnt
    if nums == q:
      qnum = cnt
    return
  for i in range(1,n+1):
    if i not in nums:
      comb(nums+[i])


comb([])

print(abs(pnum-qnum))
